#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
#curl -sI $1 | grep "HTTP" | cut -d " " -f2
curl -o /dev/null -sw "%{http_code}" $1
