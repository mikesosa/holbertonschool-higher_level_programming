#!/usr/bin/python3
"""
Script that takes in a string and sends a search request to the Star Wars API
"""
import sys
import requests


def apiRequest(data):
    """ Calling the starwars API searching names """
    request = requests.post(
        'https://swapi.co/api/people',
        params={
            'search': data}).json()
    numberOfResults = request['count']
    print('Number of results: {}'.format(numberOfResults))
    for key in request['results']:
        print(key['name'])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        apiRequest(sys.argv[1])
