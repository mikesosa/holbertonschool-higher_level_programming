#!/bin/bash
# Script that returns the size in bites of an ip
# by the info of the headers
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
