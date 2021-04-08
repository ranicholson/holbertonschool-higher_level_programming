#!/bin/bash
# Script take url and sends POST request. Displays body of response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
