#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -o /dev/null -sw "%{http_code}" $1
