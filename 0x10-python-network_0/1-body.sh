#!/bin/bash
# Script to display body of URL Request for 200 status code
curl -sL "$1" -X GET
