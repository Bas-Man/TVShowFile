#!/usr/bin/env python3

import sys
sys.path.insert(0, "..")

from tvshowfile import parser

fail = parser.Parser("test.avi")
succ = parser.Parser("test.S01E01.avi")
succ2 = parser.Parser("test.S01E01.1080p.avi")

# Example 1 testing that file was able to be parsed or not
if not fail.wasParsed():
    print("Unable to parse file: " + fail.getFilename())

# Example 1 Successful parsing of file
if succ.wasParsed:
    print("Able to parse file: " + succ.getFilename())
    print("File: " + succ.getFilename())
    print("Name: " + succ.getShowName())
    print("Season: " + succ.season)
    print("Episode: " + succ.getEpisode())
    print("SeasonEpisode: " + succ.seasonepisode)
    print("Resolution: " + succ.getResolution())
    print("Ext: " + succ.fileext)

print("\n\n")

# Example 2 Successful parsing of file
if succ2.wasParsed:
    print("Able to parse file: " + succ2.getFilename())
    print("File: " + succ2.getFilename())
    print("Name: " + succ2.getShowName())
    print("Season: " + succ2.season)
    print("Episode: " + succ2.getEpisode())
    print("SeasonEpisode: " + succ2.seasonepisode)
    print("Resolution: " + succ2.getResolution())
    print("Ext: " + succ2.fileext)
