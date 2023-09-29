#!/usr/bin/python3
"""
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    value = {'q': letter}
    p = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        if p.json():
            print('[{}] {}'.format(p.json().get('id'), p.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
