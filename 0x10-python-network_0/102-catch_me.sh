#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me and makes the server respond with "You got me!"
curl 0.0.0.0:5000/catch_me -sLX PUT -d "user_id=98" -H "Origin: DHKSchool"
