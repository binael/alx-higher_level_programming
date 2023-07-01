#!/usr/bin/python3

"""A script that takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    mail = sys.argv[2]

    data = {'email': mail}

    req = requests.post(url, data)

    print(req.text)
