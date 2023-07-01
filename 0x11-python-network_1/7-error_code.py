#!/usr/bin/python3

"""A script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
