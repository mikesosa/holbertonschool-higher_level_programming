#!/usr/bin/python3
"""
Write a Python script that takes in a string and sends a search request to the
Star Wars API
"""
import requests
import sys

if __name__ == "__main__":
    request = requests.post(
                'https://swapi.co/api/people', params={
                                'search': sys.argv[1]}).json()
    i = request['count']
    print("Number of results: {}".format(i))
    for a in request['results']:
        print(a['name'])
