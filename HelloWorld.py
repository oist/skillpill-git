#!/usr/bin/python3

import sys

def main(username, timeValue):
    print("Hello " + username)

def callFctn(args):
    if len(args) > 1:
        username = args[1]
    else:
        username = "World"

    timeValue = ""
    main(username, timeValue)

if __name__ == "__main__":
    callFctn(sys.argv)
