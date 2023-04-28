#!/usr/bin/python3
"""A python script that takes url from the command line
and displays the a header value of 'X-Request-Id'
found in the header response, utilizing urllib module
"""

if __name__ == "__main__":
    import sys, urllib.request


    with urllib.request.urlopen(sys.argv[1]) as response:
        response = response.headers
        header = "X-Request-Id"
        print(dict(response).get(header))
