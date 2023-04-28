#!/usr/bin/python3
"""A python script that uses the module
'urllib' module to fetch https://alx-intranet.hbtn.io/status
while formatting the output
"""


if __name__ == "__main__":
    import urllib.request

    my_url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(my_url) as response:
        response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf-8")))
