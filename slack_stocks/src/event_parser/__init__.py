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



