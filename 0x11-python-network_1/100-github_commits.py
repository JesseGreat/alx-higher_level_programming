#!/usr/bin/python3
"""This script prints the 10 most recent commits on the
    master branch of a GitHub repository
    by a specified user"""

import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    resp = requests.get(url)

    for commit in resp.json()[:10]:
        try:
            author_name = commit['commit']['author']['name']
            sha = commit['sha']
            print(f'{sha}: {author_name}')
        except KeyError:
            break
