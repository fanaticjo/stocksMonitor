from slack_response import slack_response

run_commands = {
    "review":
        {
            "endpoint": "/detail",
            "doc": "gives the pros cons of a stock",
            "deployed": "yes",
            "function": slack_response.review
        },
    "price": {
        "endpoint": "/stock_info",
        "doc": "gives the price and other details",
        "deployed": "done",
        "function": slack_response.stock_info
    },
    "peer":
        {
            "endpoint": "/peer_group",
            "doc": "gives the peer companies",
            "deployed": "not"
        },
    "info": {
        "endpoint": "/stock_info",
        "doc": "gives the info",
        "deployed": "done",
        "function": slack_response.stock_info
    },
    "pe": {
        "endpoint": "/avg_pe",
        "doc": "gives the pe ratio",
        "deployed": "not",
        "function": slack_response.pe
    }
}
