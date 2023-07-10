#!/usr/bin/python3
"""Defines a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square]: {}/{}".format(self.__size, self.__size)
