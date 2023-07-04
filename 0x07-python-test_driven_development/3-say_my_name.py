#!/usr/bin/python3
"""Prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """
    Prints first name and last name

    Args:
        first_name (str): string
        last_name (str, optional): string. defaults to ""

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
