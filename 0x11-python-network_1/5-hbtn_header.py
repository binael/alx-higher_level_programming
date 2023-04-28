#!/usr/bin/python3
"""A script that utilizes python 'requests' module to
fetch a website"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
