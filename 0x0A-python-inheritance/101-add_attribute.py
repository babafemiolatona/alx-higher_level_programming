#!/usr/bin/python3
"""Defines a function"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
