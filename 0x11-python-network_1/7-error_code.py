#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL, sends a request to the URL and displays the
    body of the response using requests
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
