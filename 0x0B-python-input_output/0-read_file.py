#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as f:
        read_dt = f.read()
        print(read_dt)
