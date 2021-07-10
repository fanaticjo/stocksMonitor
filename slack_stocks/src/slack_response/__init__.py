from typing import List, Dict, Union

number_mapping: Dict[int, str] = {
    0: " :zero: ",
    1: " :one: ",
    2: " :two: ",
    3: " :three: ",
    4: " :four: ",
    5: " :five: ",
    6: " :six: ",
    7: " :seven: ",
    8: " :eight: ",
    9: " :nine: ",
    10: " :keycap_ten: "
}


def make_message(data: str):
    """
    This makes slack section message
    :param data:
    :return:
    """
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": data
        }
    }


class slack_response:
    """
    This gives response in slack format
    """
    _completed = ':white_check_mark:'
    _not_completed = ':x:'

    @staticmethod
    def review(company: str, response: str):
        """
        This gives the pros and cons of the stock
        :param company:
        :param response:
        :return:
        """
        main_header: Dict[str, List[Dict[str, str]]] = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "text": f" :newspaper: Review For {company} :newspaper: ",
                        "type": "plain_text"
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }
        pro_header = [
            {
                "type": "header",
                "text": {
                    "text": " :ideograph_advantage:  PROS :ideograph_advantage: ",
                    "type": "plain_text"
                }
            }
        ]
        not_found = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f" {slack_response._not_completed} Mostly stock is out of pros {slack_response._not_completed}"
                }
            }
        ]
        pros_data: List[Dict[str, Union[Dict[str, str], str]]] = [
            make_message(f" {number_mapping.get(index)} {data} {slack_response._completed}")
            for index, data in enumerate(response.get('pro'))
        ]
        pros = pro_header + pros_data if pros_data else not_found
        cons_header = [
            {
                "type": "header",
                "text": {
                    "text": " :disappointed:   CONS :disappointed:  ",
                    "type": "plain_text"
                }
            }
        ]
        cons_data: List[Dict[str, Union[Dict[str, str], str]]] = [
            make_message(f" {number_mapping.get(index)} {data} {slack_response._not_completed}")
            for index, data in enumerate(response.get('con'))
        ]
        con = cons_header + cons_data if pros_data else not_found
        main_header['blocks'] = main_header['blocks'] + pros + con
        return main_header

    @staticmethod
    def pe(company: str, response: str):
        """
        This gives the pe in slack
        :param company:
        :param response:
        :return:
        """
        print(response)

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
    def help_response(run_commands):
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
                "text": f":point_right: *{key}* \n {run_commands.get(key).get('doc')} \n deployed: {slack_response._completed if run_commands.get(key).get('deployed') == 'done' else slack_response._not_completed} "
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
        print(response)
        return response
