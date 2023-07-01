#!/usr/bin/python3
"""
A python script that fetches and displays a website
"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as page:
        html = page.read()

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(str(html, "utf-8")))
