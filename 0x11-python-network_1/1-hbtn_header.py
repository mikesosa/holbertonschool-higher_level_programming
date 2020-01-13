#!/usr/bin/python3
"""
Write a Python script that takes in a URL
sends a request to the URL and displays the value of the X-Request-Id value
"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as r:
        print(r.getheader('X-Request-ID'))
