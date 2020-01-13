#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    """ Function that sends a post request"""
    if len(sys.argv) >= 2:
        letter = sys.argv[1]
    else:
        letter = ""
    try:
        payload = {'q': letter}
        r = requests.post(
            'http://0.0.0.0:5000/search_user',
            data=payload).json()
        if "id" in r and "name" in r:
            print('[{}] {}'.format(r['id'], r['name']))
        else:
            print("No result")
    except BaseException:
        print('Not a valid JSON')
