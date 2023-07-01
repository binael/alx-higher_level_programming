#!/usr/bin/python3

"""A script that  takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    api = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    basic = HTTPBasicAuth(username, password)

    req = requests.get(api, auth=basic)

    j_data = req.json()

    print(j_data.get('id'))
