#!/usr/bin/python3
"""Defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of a class that inherited from, the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
