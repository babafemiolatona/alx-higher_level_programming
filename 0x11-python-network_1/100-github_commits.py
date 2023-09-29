#!/usr/bin/python3
"""
    Using the GitHub API to list the last 10 commits
"""
import requests
from sys import argv


if __name__ == "__main__":
    repository_name = argv[1]
    owner_name = argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repository_name)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print("{}: {}".format(
            commit.get('sha'),
            commit.get('commit').get('author').get('name')))
