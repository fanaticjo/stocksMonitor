import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from Screener.table_parser import TableParser
from typing import Optional, Dict, List


class WebParser:
    """
    This parses screener website to get results
    """
    __WEBSITE = "https://www.screener.in"

    def __init__(self, company: str):
        self.company: str = company
        self.page_content: Optional[bytes] = None
        self.stock_info: Dict[str, str] = {}
        self.scrapper: Optional[BeautifulSoup] = None
        self.pros: List[str] = []
        self.cons: List[str] = []

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
                                                   "https://www.screener.in")
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

    def pe_comparison(self):
        """
        This compares the pe of the company with the
        :return:
        """
        peers = self.scrapper.find("section", id="peers").find("p").find_all("a")
        ctgry: Dict[str, str] = {}
        for sector_ctgry in peers:
            name: str = sector_ctgry.text
            redirect_link: str = sector_ctgry['href']
            ctgry[name.strip()] = redirect_link.strip()
        print(ctgry)
        for sector, endpoint in ctgry.items():
            print(sector)
            data = WebParser.make_request(endpoint, WebParser.__WEBSITE)
            print(TableParser().start_scrap(data).make_table())
        return self


if __name__ == "__main__":
    print(WebParser("INFY").start_scrap().scrap_stock_info().scrap_stock_info().scrap_pros_cons().pe_comparison())
