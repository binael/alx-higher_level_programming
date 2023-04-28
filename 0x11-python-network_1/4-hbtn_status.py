#!/usr/bin/python3
"""A script that utilizes python 'requests' module to
fetch a website"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(response.text.__class__))
    print("\t- content: {}".format(response.text))
