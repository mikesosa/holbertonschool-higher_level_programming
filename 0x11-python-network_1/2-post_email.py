#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from urllib import request
from urllib import parse
import sys


def urlRequest(url, email):
    """ Function that sends a post request"""
    values = {'email': email}

    data = parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))


if __name__ == "__main__":
    urlRequest(sys.argv[1], sys.argv[2])
