#!/bin/bash
# Script that displays http status code
curl -sL -H "Content-Type: application/json" -d @"$2" -X POST "$1"
