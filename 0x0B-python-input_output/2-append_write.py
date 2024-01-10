#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""

def append_write(filename="", text=""):
    """functionto append string to end of text file"""
    with open(filename, mode='a', encoding='UTF') as a_file:
        a_file.write(text)
    return len(text)
