#!/usr/bin/python3

"""A script that pulls out 10 commits from a repo
"""

if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    r = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    req = requests.get(r)

    j_data = req.json()

    counter = 0

    for data in j_data:
        sha = data.get('sha')
        author = data.get('commit').get('author').get('name')

        print('{}: {}'.format(sha, author))
        counter += 1

        if counter >= 10:
            break
