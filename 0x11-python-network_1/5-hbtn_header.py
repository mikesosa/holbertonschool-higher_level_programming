#!/usr/bin/python3
"""
Write a Python script that takes in a URL
sends a request to the URL and displays the value of the X-Request-Id value
"""
import requests
import sys

if __name__ == "__main__":
    poop = requests.get(sys.argv[1])
    print(poop.headers.get('X-Request-ID'))
