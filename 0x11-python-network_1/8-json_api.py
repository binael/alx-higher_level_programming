#!/usr/bin/python3
"""A script that utilizes python 'requests' module to
send a request to a url while printing the error code"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
