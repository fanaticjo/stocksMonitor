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


if __name__ == "__main__":
    event = {
        'body': 'dG9rZW49N3ZKY0s2SGdTd1RhSGVFdWtJb200ekluJnRlYW1faWQ9VDAyNUdIMjdKUFAmdGVhbV9kb21haW49c3RvY2thcGlzJmNoYW5uZWxfaWQ9QzAyNUtIU0NCUjgmY2hhbm5lbF9uYW1lPWdlbmVyYWwmdXNlcl9pZD1VMDI1Q1I4RlA0TiZ1c2VyX25hbWU9Ymlzd2FqaXQubW9oYXBhdHJhNjUmY29tbWFuZD0lMkZzdG9ja3MmdGV4dD1JTkZZK3ByaWNlJmFwaV9hcHBfaWQ9QTAyNVk3Ujg2QzkmaXNfZW50ZXJwcmlzZV9pbnN0YWxsPWZhbHNlJnJlc3BvbnNlX3VybD1odHRwcyUzQSUyRiUyRmhvb2tzLnNsYWNrLmNvbSUyRmNvbW1hbmRzJTJGVDAyNUdIMjdKUFAlMkYyMjAwMzk5OTIxODE1JTJGRGI1OTUyU29Bd0pWQXk2aG5zVlJpWlZMJnRyaWdnZXJfaWQ9MjIxMjA5OTEwMzczMy4yMTg2NTgwMjU2ODA1LmRiODg2OGRhNWVkZTgzMmQ4YjFhMzdjM2UzMjFmZGYy',
        'isBase64Encoded': True
    }
    lambda_handler(event, 1)
