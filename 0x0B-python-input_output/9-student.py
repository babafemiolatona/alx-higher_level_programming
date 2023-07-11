#!/usr/bin/python3
"""A class that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object"""
        result = {}

        for attr, value in vars(self).items():
            if isinstance(value, (list, dict, str, int, bool)):
                result[attr] = value
            elif hasattr(value, '__dict__'):
                result[attr] = self._to_json_recursive(value)
        return result

    def _to_json_recursive(self, obj):
        """Handle nested objects"""
        result = {}

        for attr, value in vars(obj).items():
            if isinstance(value, (list, dict, str, int, bool)):
                result[attr] = value
            elif hasattr(value, '__dict__'):
                result[attr] = self._to_json_recursive(value)

        return result
