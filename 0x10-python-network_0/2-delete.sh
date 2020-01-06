#!/bin/bash
# Bash script that takes in a URL, sends a DELETE request and posts the reponse
curl -sL -X DELETE "$1"
