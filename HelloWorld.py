#!/usr/bin/python3

import sys
import time

def main(timeValue):
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

    print(greeting)

def callFctn(args):
    if len(args) > 1:
        timeValue = time.strptime(args[1], "%H:%M")
    else:
        timeValue = ""
    
    main(timeValue)

if __name__ == "__main__":
    callFctn(sys.argv)
