#!/usr/bin/env python3

import sys
sys.path.insert(0, "..")

import tvshowfile

obj = tvshowfile.TVShowFile.TVShowFileParser("test.avi")

if obj is False:
    print("nothing here\n")
else:
    print(obj.filename + "\n")