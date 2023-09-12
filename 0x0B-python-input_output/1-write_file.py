#!/usr/bin/python3
"""
Program 
"""


def write_file(filename="", text=""):
    """ func """
    if filename == "":
        return
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
