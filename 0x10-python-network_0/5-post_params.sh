#!/bin/bash
#  URL, sends a POST request to the passed URL, and displays reponse
curl -sH -X POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
