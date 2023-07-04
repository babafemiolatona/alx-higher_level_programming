#!/usr/bin/python3
"""Sums two integers or floats"""


def add_integer(a, b=98):
    """
    Sums two integers or floats

    Args:
        a (number): float or int
        b (number, optional): float or int. defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: sum
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
