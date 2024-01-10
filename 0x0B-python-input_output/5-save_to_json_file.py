#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation
"""

def save_to_json_file(my_obj, filename):
    """module save_to_json_file
    accepts Python object and sends JSON representation to file"""
    
    import json

    with open(filename, mode="W", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
