#!/bin/bash
# Script  that takes in a URL and displays all HTTP methods the server will accept.
curl -sIL "$1" | grep -i "allow" | cut -d ":" -f2 | cut -b 2-
