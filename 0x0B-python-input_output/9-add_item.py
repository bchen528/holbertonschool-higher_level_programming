#!/usr/bin/python3
from sys import argv
"""access commandline arguments"""
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""create object from JSON file"""
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""writes an object to text file, using JSON representation"""

filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except:
    content = []

for i in range(1, len(argv)):
    content.append(argv[i])
save_to_json_file(content, filename)
