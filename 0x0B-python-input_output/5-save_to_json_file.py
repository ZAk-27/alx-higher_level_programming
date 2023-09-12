#!/usr/bin/python3
"""
jason save 
"""
import json


def save_to_json_file(my_obj, filename):
    """ printing file """
    if filename == "":
        return
    with open(filename, "w") as f:
        json.dump(my_obj, f)
