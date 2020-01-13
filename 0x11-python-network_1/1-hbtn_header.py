#!/usr/bin/python3
"""
Write a Python script that takes in a URL
sends a request to the URL and displays the value of the X-Request-Id value
"""
from urllib import request
import sys


def urlRequest(data):
    """ Function that makes a request to a url. 67 days left """
    response = request.urlopen(data)
    headers = response.info()
    print(headers['X-Request-Id'])

if __name__ == "__main__":
    urlRequest(sys.argv[1])
