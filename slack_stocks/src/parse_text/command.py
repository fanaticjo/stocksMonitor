from typing import Optional, Dict

from requests import Response

import requests
from parse_text import run_commands
from slack_response import slack_response


class command:
    def __init__(self, text: str, conn: str) -> None:
        self.text = text
        self.conn: str = conn

    def make_request(self, method: str, endpoint: str):
        """
        this makes the request call
        :return:
        """
        url: str = f"{self.conn}/{endpoint}"
        print(url)
        response: Response = requests.request(
            method=method,
            url=url
        )
        if response.status_code == 200:
            return response.json()
        else:
            return " *Check if the company exists in BSE/NSE*  :x: "

    def create_request(self):
        """
        This parses the text and calls the stock api's
        :return:
        """
        try:
            stock_name, request = self.text.split(" ")
            print(stock_name)
            print(request)
            if request in run_commands.keys():
                endpoint: str = run_commands.get(request).get('endpoint')
                url_maker: str = f"stocks/{stock_name}{endpoint}"
                print(url_maker)
                response: Optional[str, Dict[str, str]] = self.make_request(method="GET", endpoint=url_maker)
                if isinstance(response, dict):
                    print(response)
                    api_response: Dict[str, str] = slack_response.stock_info(stock_name, response.get("message"))
                    print(api_response)
                    return api_response
            else:
                return "release in progress"
        except ValueError as e:
            return slack_response.help_response()
        except KeyError as e:
            return slack_response.help_response()
