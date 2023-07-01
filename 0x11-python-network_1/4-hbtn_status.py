#!/usr/bin/python3

"""A script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    req = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
