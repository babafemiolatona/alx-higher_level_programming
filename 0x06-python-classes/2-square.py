#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """A class that defines a Square"""
    def __init__(self, size=0):
        """Initializes a new instance of the Square class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
