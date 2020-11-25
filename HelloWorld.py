#!/usr/bin/python3

import sys
import time

def main(timeValue):
    morningStart = 4
    eveningStart = 18
    greeting = ""
    hour = timeValue.tm_hour
    if (hour >= morningStart) & (hour < 12):
        greeting = "Good morning"
    elif (hour >= 12) & (hour < eveningStart):
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print(greeting)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        timeValue = time.strptime(sys.argv[1], "%Y_%m_%d-%H:%M")
    else:
        timeValue = time.localtime(time.time())
    main(timeValue)
