from bs4 import BeautifulSoup


def scrap_website(html_content):
    return BeautifulSoup(html_content, 'html.parser')
