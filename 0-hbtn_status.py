#!/usr/bin/python3
"""
A python script that fetches and displays a website
"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    req = url.request.Request(url)

    with urllib.request.urlopen(url) as page:
        html = page.read()

    print(type(page))
