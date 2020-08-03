#!/usr/bin/env python3

# This program demonstrate obtaining show name without year information
import sys
import json

sys.path.insert(0, "..")


with open('exceptionlist.json', 'r') as fhandle:
    newList = json.load(fhandle)

print(newList)
