#!/usr/bin/python3
"""
Program 
"""


def read_file(filename=""):
    """ prints """
    if filename == "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
