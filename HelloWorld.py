#!/usr/bin/python3

import sys
import time

def getGreeting(timeValue):
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
    return greeting


def main(username, timeValue):
    greeting = getGreeting(timeValue)
    print(greeting + " " + username)

def callFctn(args):
    username = "World"
    
    if len(args) > 1:
        try:
            timeValue = time.strptime(args[1], "%H:%M")
        except:
            timeValue = ""
    else:
        timeValue = ""

    main(username, timeValue)

if __name__ == "__main__":
    callFctn(sys.argv)
