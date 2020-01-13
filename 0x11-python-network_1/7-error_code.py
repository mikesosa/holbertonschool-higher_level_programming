#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import sys
import requests


def urlRequest(url):
    """ Function that sends a post request I hated padresehijos lmao"""
    r = requests.get(url)
    padresehijos = r.status_code
    if padresehijos >= 400:
        print('Error code: {}'.format(padresehijos))
    else:
        print(r.text)


if __name__ == "__main__":
    urlRequest(sys.argv[1])
