#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -o /dev/null -sw "%{http_code}" $1
