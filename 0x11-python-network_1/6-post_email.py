#!/usr/bin/python3
"""
Write a Python script that takes in a URL
sends a request to the URL and displays the value of the X-Request-Id value
"""
import sys
import requests


def urlRequest(url, email):
    """ Function that makes a request to a url. 67 days left """
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)


if __name__ == "__main__":
    urlRequest(sys.argv[1], sys.argv[2])
