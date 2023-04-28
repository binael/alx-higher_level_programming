#!/usr/bin/python3
"""Script that sends a GET request to a website
and displays the body or the error code
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            response = response.read()
            print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
