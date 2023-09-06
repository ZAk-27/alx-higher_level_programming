#!/usr/bin/python3
"""

 Rectangle class that defines a rectangle

"""


class Rectangle:
    """
    Creating Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initializing variables
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("width mst be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets width value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
