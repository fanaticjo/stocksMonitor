import base64
import json
from urllib import parse
from typing import Optional, Dict


class EventParser:
    """
    This gets the event from the lambda handler
    """
    _encoded = 'isBase64Encoded'
    _key = 'body'

    def __call__(self, event, context):
        """
        This parses the event class
        :param event:
        :param context:
        :return:
        """
        if event.get(EventParser._encoded):
            body: Dict[str, str] = dict(parse.parse_qsl(base64.b64decode(event.get(EventParser._key)).decode('ascii')))
            self.body = body
        else:
            self.body = event.get(EventParser._key)

    def __init__(self):
        self._body: Optional[Dict[str, str]] = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value


if __name__ == "__main__":
    event = {
        'body': 'dG9rZW49N3ZKY0s2SGdTd1RhSGVFdWtJb200ekluJnRlYW1faWQ9VDAyNUdIMjdKUFAmdGVhbV9kb21haW49c3RvY2thcGlzJmNoYW5uZWxfaWQ9QzAyNUtIU0NCUjgmY2hhbm5lbF9uYW1lPWdlbmVyYWwmdXNlcl9pZD1VMDI1Q1I4RlA0TiZ1c2VyX25hbWU9Ymlzd2FqaXQubW9oYXBhdHJhNjUmY29tbWFuZD0lMkZzdG9ja3MmdGV4dD1pbmZ5JmFwaV9hcHBfaWQ9QTAyNVk3Ujg2QzkmaXNfZW50ZXJwcmlzZV9pbnN0YWxsPWZhbHNlJnJlc3BvbnNlX3VybD1odHRwcyUzQSUyRiUyRmhvb2tzLnNsYWNrLmNvbSUyRmNvbW1hbmRzJTJGVDAyNUdIMjdKUFAlMkYyMjE0MDkxOTUxMTg3JTJGSzRoV0tEMHhVNElXbGFzWENxZjhLOVd5JnRyaWdnZXJfaWQ9MjIxMDg2NDM4NzI1My4yMTg2NTgwMjU2ODA1LjU4Zjc1NzBkNjAyZTljZjVkODRmOTIzZTc1OGU4NTU3',
        'isBase64Encoded': True
    }
    event_parser: EventParser = EventParser()
    event_parser(event, '1')
    print(event_parser.body)
