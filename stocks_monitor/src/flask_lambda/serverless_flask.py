"""
 This runs for python 3.8

"""

import sys
import base64
from urllib.parse import urlencode


from flask import Flask
from io import StringIO

from werkzeug.wrappers import Request


def make_environ(event):
    environ = {
        'HTTP_HOST': '',
        'HTTP_X_FORWARDED_PORT': '',
        'HTTP_X_FORWARDED_PROTO': ''
    }

    if event['headers'] is not None:
        for hdr_name, hdr_value in event['headers'].items():
            hdr_name = hdr_name.replace('-', '_').upper()
            if hdr_name in ['CONTENT_TYPE', 'CONTENT_LENGTH']:
                environ[hdr_name] = hdr_value
                continue

            http_hdr_name = 'HTTP_%s' % hdr_name
            environ[http_hdr_name] = hdr_value

    qs = event['queryStringParameters']

    environ['REQUEST_METHOD'] = event['httpMethod']
    environ['PATH_INFO'] = event['path']
    environ['QUERY_STRING'] = urlencode(qs) if qs else ''
    environ['REMOTE_ADDR'] = event['requestContext']['identity']['sourceIp']
    environ['HOST'] = '%(HTTP_HOST)s:%(HTTP_X_FORWARDED_PORT)s' % environ
    environ['SCRIPT_NAME'] = ''

    environ['SERVER_PORT'] = environ['HTTP_X_FORWARDED_PORT']
    environ['SERVER_PROTOCOL'] = 'HTTP/1.1'

    environ['CONTENT_LENGTH'] = str(
        len(event['body']) if event['body'] else ''
    )

    environ['wsgi.url_scheme'] = environ['HTTP_X_FORWARDED_PROTO']
    environ['wsgi.input'] = StringIO(event['body'] or '')
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.multithread'] = False
    environ['wsgi.run_once'] = True
    environ['wsgi.multiprocess'] = False

    Request(environ)

    return environ


class LambdaResponse(object):
    def __init__(self):
        self.status = None
        self.response_headers = None

    def start_response(self, status, response_headers, exc_info=None):
        self.status = int(status[:3])
        self.response_headers = dict(response_headers)


class FlaskLambda(Flask):
    def __call__(self, event, context):
        if 'httpMethod' not in event:
            #print("here")
            # In this "context" `event` is `environ` and
            # `context` is `start_response`, meaning the request didn't
            # occur via API Gateway and Lambda
            return super(FlaskLambda, self).__call__(event, context)

        response = LambdaResponse()

        body = next(self.wsgi_app(
            make_environ(event),
            response.start_response
        ))

        res = {
            'statusCode': response.status,
            'headers': response.response_headers,
            'body': body.decode('utf-8'),
            'isBase64Encoded': False
        }
        print("--------------------")
        print(res)
        print(type(res))
        return res





