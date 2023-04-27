#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response

status=$(curl -s -I "$1" | head -n 1 | cut -d " " -f 2)

if [ "$status" != 200 ]; then
	exit
fi

curl -sL "$1"
