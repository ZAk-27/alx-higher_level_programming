#!/usr/bin/python3
"""
Returning True if the objct is an inst. of a class that inherited from
the specified class
"""


def inherits_from(obj, a_class):
    """ return True if the obj is an instance of a class that inherited"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
