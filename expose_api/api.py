from typing import Dict

from Screener.web_parser import WebParser
from expose_api import app
from flask import request, jsonify, make_response


def make_error_response(message):
    return make_response(
        jsonify({
            "message": message
        }),
        404
    )


@app.route("/")
def hello():
    return "hello"


@app.route("/stocks/<string:name>/stock_info", methods=["GET"])
def get_stock_info(name: str):
    """
    This gets the stock info
    :param name:
    :return:
    """
    if request.method == "GET":
        stock_info: Dict[str, str] = WebParser(name).start_scrap().scrap_stock_info().get_stock_info
        return make_response(
            jsonify(
                {
                    "message": stock_info
                }
            ),
            200
        )
    else:
        make_error_response("Only get operation supported")


@app.route("/stocks/<string:name>/detail", methods=["GET"])
def get_pros_cons(name: str):
    """
    This get's the pros and cons of the stock's
    :param name:
    :return:
    """
    if request.method == "GET":
        pros_cons = WebParser(name).start_scrap().scrap_pros_cons()
        pro = pros_cons.get_pro
        cons = pros_cons.get_cons
        return make_response(
            jsonify({
                "company": name,
                "pro": pro,
                "con": cons
            }),
            200
        )
    else:
        make_error_response("Only get operation supported")


@app.route("/stocks/<string:name>/peer_group", methods=["GET"])
def get_peer_group(name: str):
    """
    This get's the sector companies
    :return:
    """
    if request.method == "GET":
        peer_group = WebParser(name).start_scrap().set_sector_information().get_sector_data
        return make_response(
            jsonify(
                {
                    "name":name,
                    "peer_companies":peer_group
                }
            ),
            200
        )
    else:
        make_error_response("only get request is supported")
