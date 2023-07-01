#!/usr/bin/python3

"""
A script  that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as page:
        print(page.headers['X-Request-Id'])
