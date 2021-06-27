from typing import List, Dict

from parse_text import run_commands


class slack_response:
    """
    This gives response in slack format
    """
    _completed=':white_check_mark:'
    _not_completed=':x:'

    @staticmethod
    def stock_info(company: str, response: str):
        """
        This creates the slack message for stock info
        :param company:
        :param response:
        :return:
        """
        response: Dict[str, List[Dict[str, str]]] = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "text": f" :large_green_square: *Company* \n {company} ",
                        "type": "plain_text"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :book: *Book Value:* \n The value is *{response.get('Book Value')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :coin: *Current Price:* \n The value is *{response.get('Current Price')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :moneybag: *Dividend Yield:* \n The value is *{response.get('Dividend Yield')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :face_with_monocle:  *Face Value:* \n The value is *{response.get('Face Value')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :chart_with_upwards_trend:  *High / Low:* \n The value is *{response.get('High / Low')}*  :chart_with_downwards_trend: "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :billed_cap:  *Market Cap:* \n The value is *{response.get('Market Cap')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :arrows_clockwise: *ROCE:* \n The value is *{response.get('ROCE')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :racehorse:  *ROE:* \n The value is *{response.get('ROE')}* "
                    }

                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f" :chart:  *Stock P/E:* \n The value is *{response.get('Stock P/E')}* "
                    }

                }
            ]

        }
        return response

    @staticmethod
    def help_response():
        response: Dict[str, List[Dict[str, str]]] = {
            "blocks": [
                {
                    "type": "header",
                    "text":
                        {
                            "text": " :money_with_wings: Stocks Info Commands :money_mouth_face: ",
                            "type": "plain_text"
                        }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": " :loud_sound: *Mutual Fund will Come Soon* :loud_sound:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Commands:*"
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }
        commands: List[Dict[str, str]] = [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":point_right: *{key}* \n {run_commands.get(key).get('doc')} \n deployed: {slack_response._completed if  run_commands.get(key).get('deployed')=='done' else slack_response._not_completed} "
            }
        } for key in run_commands.keys()]
        release_date: List[Dict[str, str]] = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Will release the commands by next week \n :pager: *biswajit_mohapatra*"
                }
            }
        ]
        example: List[Dict[str, str]] = [
            {
                "type": "divider",

            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": " :white_check_mark: Examples \n /stocks INFY price"
                }
            },
            {
                "type": "divider",
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": " *API are also available* \n :credit_card:(Paid) Contact :pager: biswajit_mohapatra "
                }
            }
        ]
        response['blocks'] = response['blocks'] + commands + release_date + example
        return response
