#!/usr/bin/python3
"""Defines a Square"""


class Square:
    def __init__(self, size=0):
        """Initializes a new instance of the Square class"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2
