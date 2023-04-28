#!/usr/bin/python3
"""A script that utilizes python 'requests' module to
send a post request taking a URL and an email"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    params = {'email': sys.argv[2]}

    response = requests.post(url, data=params)
    print(response.text)
