#!/usr/bin/python3
"""A python script that takes url from the command line
and displays the a header value of 'X-Request-Id'
found in the header response, utilizing urllib module
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    my_url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(my_url) as response:
        response = response.headers
        header = "X-Request-Id"
        print(dict(response).get(header))
