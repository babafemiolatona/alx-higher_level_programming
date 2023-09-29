#!/usr/bin/python3
"""
This script takes in a URL, sends a request and
displays the value of the X-Request-Id
"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        html = response.info()
        print(html['X-Request-Id'])
