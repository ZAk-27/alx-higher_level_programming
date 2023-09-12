#!/usr/bin/python3
"""
returns an object string
"""
import json


def from_json_string(my_str):
    """ returns func """
    return json.loads(my_str)
