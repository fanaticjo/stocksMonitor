import json
from event_parser import EventParser
from parse_text.command import command
import os


def lambda_handler(event, context):
    event_parser: EventParser = EventParser()
    event_parser(event, context)
    body = event_parser.body.get('text')
    conn = os.environ['endpoint']
    response = command(body, conn).create_request()
    print(response)
    return response



