#!/usr/bin/python3

import sys

def main(username):
    print("Hello " + username)

def callFctn(args):
    username = ""
    if (len(args) > 1):
        username = args[1]
    else:
        username = "World"
        
    main(username)

if __name__ == "__main__":
    callFctn(sys.argv)
