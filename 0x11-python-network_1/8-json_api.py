#!/usr/bin/python3

"""A script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': ''}

    if len(sys.argv) >= 2:
        payload = {'q': sys.argv[1]}

    req = requests.post(url, data=payload)

    try:
        form = req.json()
    except ValueError:
        print('Not a valid JSON')
    else:
        if form:
            print('[{}] {}'.format(form.get('id'), form.get('name')))
        else:
            print('No result')
