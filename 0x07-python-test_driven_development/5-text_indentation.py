#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Created new lines based on ? : or ."""
    buf = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        buf += letter
        if letter == "." or letter == "?" or letter == ":":
            while buf[0] == " ":
                buf = buf[1:]
            print(buf)
            print()
            buf = ""
    if len(buf) != 0:
        try:
            while buf[0] == " ":
                buf = buf[1:]
        except Exception:
            pass
        print(buf, end="")
