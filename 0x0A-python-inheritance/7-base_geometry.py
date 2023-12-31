#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """ class BaseGeometry"""
    def integer_validator(self, name, value):
        """ int validtor """
        if not type(value) is int:
            raise TypeError(str(name) + " must be an int")
        if value <= 0:
            raise ValueError(str(name) + " must be gr8er than 0")

    def area(self):
        """ public instance method not implemented"""
        raise Exception("area() is not implemented")
