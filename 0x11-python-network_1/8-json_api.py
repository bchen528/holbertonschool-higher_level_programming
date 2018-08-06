#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
    """
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.get(url)
    if len(argv) == 2:
        r = requests.post(url, data={'q': argv[1]})
    else:
        r = requests.post(url, data={'q': ""})
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except:
        print("Not a valid JSON")
