#!/usr/bin/python3
"""
json file
"""
import json


def load_from_json_file(filename):
    """ printg func """
    if filename == "":
        return
    with open(filename, "r") as f:
        return json.load(f)
