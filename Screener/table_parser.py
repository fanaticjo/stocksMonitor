from bs4 import BeautifulSoup
from typing import List, Optional, Dict
from parser.parse import scrap_website


class TableParser:
    def __init__(self):
        self.scrapper = None
        self.tbl: Dict[str, Dict[str, str]] = {}
        self.headers: List[List[str, Optional[str]]] = []

    @staticmethod
    def search_table(html_content, search=None, search_element=None):
        """
        This creates a list of tuple from the html table parsed by beautiful soup
        :return:
        """
        soup = scrap_website(html_content)
        if search_element == "class":
            print("searching in class type")
            return soup.find("table", class_=search)
        elif search_element == "id":
            print("searching in id type")
            return soup.find("table", id=search)
        else:
            print("searching without identifier")
            return soup.find("table")

    def start_scrap(self, html_content):
        self.scrapper = TableParser.search_table(html_content).find_all("tr")
        return self

    def find_headers(self):
        """
        This find the headers from the html table
        :return:
        """
        for header_html in self.scrapper[0].find_all("th"):
            header = header_html.text.strip().split("\n")
            if len(header) > 1:
                self.headers.append([header[0], header[1].strip()])
            else:
                self.headers.append(header)
        return self

    def make_table(self):
        """
        This creates the table content
        :return:
        """
        self.find_headers()
        for data_html in self.scrapper[1:]:
            tmp_data: Dict[str, str] = {}
            for i, data in enumerate(data_html.find_all("td")):
                tmp_data[self.headers[i][0]] = data.text.strip().replace("\n", "")
            self.tbl[tmp_data.get("Name")] = tmp_data
        print(self.tbl)
        return self
