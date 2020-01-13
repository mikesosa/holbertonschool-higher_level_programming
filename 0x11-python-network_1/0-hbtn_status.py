#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import request


def urlRequest():
    """ Function that makes a request to a url. Its 6:15am """
    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))

if __name__ == "__main__":
    urlRequest()
