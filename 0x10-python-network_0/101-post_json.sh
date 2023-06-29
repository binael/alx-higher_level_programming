#!/bin/bash
# Script that displays http status code
curl -sL --data-urlencode @"$2" -X POST "$1"
