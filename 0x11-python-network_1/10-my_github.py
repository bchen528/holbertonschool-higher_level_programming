#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses the
Github API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes your Github credentials (username and password) and uses the
    Github API to display your id
    """
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get('id'))
    except:
        pass
