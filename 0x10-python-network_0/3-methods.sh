#!/bin/bash
# sends a GET request to the URL passed and displays the allows
curl -sLI -X GET "$1" | grep "Allow"  | cut -c8-
