#!/usr/bin/python3
"""A class that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object"""
        if attrs is None:
            attrs = vars(self).keys()
        result = {}

        for attr, val in vars(self).items():
            if attr in attrs and isinstance(val, (list, dict, str, int, bool)):
                result[attr] = val
            elif attr in attrs and hasattr(val, '__dict__'):
                result[attrs] = self._to_json_recursive(val)
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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for attr, value in json.items():
            setattr(self, attr, value)
