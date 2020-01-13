#!/usr/bin/python3
"""
Write a Python script that takes your Github credentials (username and
password) and uses the Github API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    try:
        toothpaste = requests.get('https://api.github.com/user',
                                  auth=(sys.argv[1], sys.argv[2])).json()
        if "id" in toothpaste:
            print(toothpaste["id"])
        else:
            print("None")
    except:
        print("None")
