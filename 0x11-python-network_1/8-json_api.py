#!/usr/bin/python3
"""A script that utilizes python 'requests' module to
send a post request to a url(http://0.0.0.0:5000/search_user)
with parameters and output results only received in
json format"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    
    if sys.argv[1]:
        data = {"q": sys.argv[1]}
    else:
        data = {"q": ""}

    response = requests.post(url, data=data)

    try:
        j_file = response.json()
        if j_file is None:
            print("No result")
        else:
            print("[{}] {}".format(j_file.get("id"), j_file.get("name")))
    except Exception:
        print("Not a valid json file")
