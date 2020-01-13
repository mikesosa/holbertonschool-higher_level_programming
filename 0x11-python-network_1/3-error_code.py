#!/usr/bin/python3
"""
Sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
import sys
from urllib import request
from urllib import error


def urlRequest(url):
    """ Function that catches errors"""
    try:
        with request.urlopen(url) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == "__main__":
    urlRequest(sys.argv[1])
