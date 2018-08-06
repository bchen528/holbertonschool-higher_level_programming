#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a string and sends a search request to the Star Wars API
    """
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])

    r = requests.get(url)
    try:
        res_list = r.json().get('results')
        res_count = r.json().get('count')
        print("Number of results: {}".format(res_count))
        for i in range(len(res_list)):
            print(res_list[i].get('name'))
    except:
        pass
