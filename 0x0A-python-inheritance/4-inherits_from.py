#!/usr/bin/python3
"""Defines a class"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
