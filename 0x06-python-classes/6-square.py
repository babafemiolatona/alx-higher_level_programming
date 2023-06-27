#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class"""
        self.__size = size
        self.__position = position

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

    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    def position(self, value):
        """Sets the position of the square"""
        if not (isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character "#" in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("#" * self.__size)
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
