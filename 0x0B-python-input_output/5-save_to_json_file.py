#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """module save_to_json_file
    accepts Python object and sends JSON representation to file"""
    with open(filename, mode="W", encoding='utf-8') as a_file:
        json.dumps(my_obj, a_file)
