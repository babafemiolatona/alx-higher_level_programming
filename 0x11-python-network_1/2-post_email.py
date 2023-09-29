#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request to the passed"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    encoded_data = parse.urlencode(data).encode('ascii')
    with request.urlopen(url, data=encoded_data) as response:
        html = response.read()
        print(html.decode('utf-8'))
