#!/usr/bin/python3

"""A script  that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    from urllib.error import HTTPError

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        print(page.decode('utf-8'))
