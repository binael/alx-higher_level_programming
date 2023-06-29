#!/bin/bash
# Script that displays http status code
curl -sIL "$1" -w "%{http_code}" -o /dev/null
