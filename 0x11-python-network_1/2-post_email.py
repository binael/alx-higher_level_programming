#!/usr/bin/python3
"""A python script that takes from the command line
a URL, an email and a password and sends a post request.
Then displays the body of the response"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        response = response.read()
        print(response.decode('utf-8'))
