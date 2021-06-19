import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from Screener.table_parser import TableParser
from typing import Optional, Dict, List, Union, Tuple
from statistics import mean


class WebParser:
    """
    This parses screener website to get results
    """
    __WEBSITE = "https://www.screener.in/"

    def __init__(self, company: str):
        self.company: str = company
        self.page_content: Optional[bytes] = None
        self.stock_info: Dict[str, str] = {}
        self.scrapper: Optional[BeautifulSoup] = None
        self.pros: List[str] = []
        self.cons: List[str] = []
        self.sector_data: Dict[str, Dict[str, str]] = {}
        self.profit_loss: Dict[str, Dict[str, str]] = {}
        self.sector_pe: Dict[str, float] = {}


    @property
    def get_sector_pe_avg(self):
        """
        This returns the sector avg
        :return:
        """
        return self.sector_pe

    @property
    def get_pro(self):
        """
        this gets the pros of the stock
        :return:
        """
        return self.pros

    @property
    def get_cons(self):
        """
        this gets the cons of the stock
        :return:
        """
        return self.cons

    @property
    def get_sector_data(self):
        """
        This returns the sector and the related stocks for the asked stock
        :return:
        """
        return self.sector_data

    @property
    def get_stock_info(self):
        """
        This gets the stock info
        :return:
        """
        return self.stock_info

    @staticmethod
    def make_request(endpoint, http=None):
        """
        This makes request to the screener website
        :return:
        """
        hit_request: str = f"{http}/{endpoint}"
        response: requests.models.Response = requests.get(hit_request)
        if response.status_code == 200:
            return response.content
        else:
            raise

    @staticmethod
    def scrap_website(html_content):
        return BeautifulSoup(html_content, 'html.parser')

    def start_scrap(self):
        """
        This starts the scrapping of the website
        :return:
        """
        self.page_content = WebParser.make_request(f"/company/{self.company}/consolidated/#analysis",
                                                   WebParser.__WEBSITE)
        self.scrapper = WebParser.scrap_website(self.page_content)
        return self

    def scrap_stock_info(self):
        """
        This assigns the basic stocks values from the screener website
        :return:
        """
        web_details = self.scrapper.find('div', class_="company-ratios").findAll("li")
        for stock_elements in web_details:
            name = stock_elements.find("span", class_="name")
            value = stock_elements.find("span", class_="number")
            self.stock_info[name.text.strip()] = value.text.strip()
        return self

    def scrap_pros_cons(self):
        """
        This scraps pros and cons
        :return:
        """
        pros_cons = self.scrapper.find("section", id="analysis")
        self.pros = [pro.text for pro in pros_cons.find("div", class_="pros").find("ul") if
                     not isinstance(pro, NavigableString)]
        self.cons = [con.text for con in pros_cons.find("div", class_="cons").find("ul") if
                     not isinstance(con, NavigableString)]
        return self

    def set_sector_information(self):
        """
        This finds the related sector to that company and its related stocks
        :return:
        """
        peers = self.scrapper.find("section", id="peers").find("p").find_all("a")
        ctgry: Dict[str, Union[str, Dict[str, str]]] = {}
        for sector_ctgry in peers:
            name: str = sector_ctgry.text
            redirect_link: str = sector_ctgry['href']
            ctgry[name.strip()] = redirect_link.strip()
        for sector, endpoint in ctgry.items():
            data = WebParser.make_request(endpoint, WebParser.__WEBSITE)
            table_data = TableParser().start_scrap(data).make_table().get_tbl
            self.sector_data[sector] = {
                "companies": table_data
            }
        return self

    def set_profit_loss(self):
        """
        This gets the profit loss for that company
        :return:
        """
        profit_loss = self.scrapper.find("section", id="profit-loss").find_all("table", class_="ranges-table")
        for x in profit_loss:
            header = x.find("th").text.strip()
            data = x.find_all("td")
            self.profit_loss[header] = {i.text.strip(): j.text.strip() for i, j in zip(data[::2], data[1::2])}
        return self

    def set_sector_pe(self):
        """
        this gives the avg sector pe for
        :return:
        """
        for sector, companies in self.sector_data.items():
            p_e: float = mean([float(value.get("P/E")) for name, value in companies.get("companies").items()])
            self.sector_pe[sector] = p_e
        return self



if __name__ == "__main__":
    print(WebParser("INFY").start_scrap().set_sector_information().set_sector_pe().get_sector_pe_avg)
