#!/usr/bin/python3
"""Locked Class with no class or object attribute"""


class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
