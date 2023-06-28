#!/usr/bin/bash
# A script that sends the size of the content of a URL request
curl -sL "$1" | wc -c
