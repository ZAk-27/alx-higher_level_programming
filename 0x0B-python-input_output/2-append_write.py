#!/usr/bin/python3
"""
Program 
"""


def append_write(filename="", text=""):
    """ write func """
    if filename == "":
        return
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
