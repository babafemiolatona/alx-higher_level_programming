#!/usr/bin/python3
"""Defines a function for JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    result = {}

    for attr, value in vars(obj).items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value
        elif hasattr(value, '__dict__'):
            result[attr] = class_to_json(value)
    return result
