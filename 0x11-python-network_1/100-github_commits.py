#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""
import requests
import sys

repo = sys.argv[1]
owner = sys.argv[2]
r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
if r.status_code == 200:
    commits = r.json()
    count = 0
    for commit in commits:
        commit_sha = commit.get('sha')
        commit_author = commit.get('commit').get('author').get('name')
        print(f"{commit_sha} {commit_author}")
        count += 1
        if count == 10:
            break
