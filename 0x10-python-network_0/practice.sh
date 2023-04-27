#!/bin/bash

# script

status=$(curl -s -I "$1" | head -n 1 | cut -d " " -f 2)

if [ "$status" != 200 ]; then
	exit
fi

curl -s -L "$1" | wc -c
