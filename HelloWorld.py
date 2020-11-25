#!/usr/bin/python3

import sys
import time

def main(username, timeValue):
    morningStart = 4
    eveningStart = 18
    greeting = ""
    try:
        hour = timeValue.tm_hour
        if (hour >= morningStart) & (hour < 12):
            greeting = "Good morning"
        elif (hour >= 12) & (hour < eveningStart):
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
    except:
        greeting = "Hello"
        pass
    print(greeting + " " + username)

def callFctn(args):
    username = ""
    if (len(args) > 1):
        username = args[1]
    else:
        username = "World"

    if len(args) > 2:
        timeValue = time.strptime(args[2], "%H:%M")
    else:
        timeValue = ""

    main(username, timeValue)

if __name__ == "__main__":
    callFctn(sys.argv)

