#!/usr/bin/python3
"""Prints a square with the character #"""


def print_square(size):
    """Prints a square with the character #"""
    square = ""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for c in range(size):
        square += "#" * size + "\n"
    print(square, end="")
