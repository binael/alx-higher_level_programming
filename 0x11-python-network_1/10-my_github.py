#!/usr/bin/python3
"""A script that utilizes python 'requests' module to
get a github ID
INPUTS: GH username, GH token, GH api (url)"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
