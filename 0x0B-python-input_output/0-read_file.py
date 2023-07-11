#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file)
