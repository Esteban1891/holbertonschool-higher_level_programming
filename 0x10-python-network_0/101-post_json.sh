#!/bin/bash
# Sends a POST request to a URL with the contents of a JSON file
curl $1 -sX POST -H "Content-Type: application/json" -d @$2
