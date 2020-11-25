#!/usr/bin/python3

import sys

def main(username, timeValue):
    print("Hello World")

def callFctn(args):
    username = "World"
    timeValue = ""
    main(username, timeValue)

if __name__ == "__main__":
    callFctn(sys.argv)
