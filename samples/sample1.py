#!/usr/bin/env python3

import sys
sys.path.insert(0, "..")

from tvshowfile import parser

fail = parser.Parser("test.avi")
succ = parser.Parser("test.S01E01.avi")
succ2 = parser.Parser("test.S01E01.1080p.avi")

# Example 1 testing that file was able to be parsed or not
if not fail.wasParsed:
    print("Unable to parse file: " + fail.fileName + "\n")

# Example 1 Successful parsing of file
if succ.wasParsed:
    print("Able to parse file: " + succ.fileName)
    print("File: " + succ.fileName)
    print("Name: " + succ.showName)
    print("Season: " + succ.season)
    print("Episode: " + succ.episode)
    print("SeasonEpisode: " + succ.seasonEpisode)
    print("Resolution: " + succ.getResolution())
    print("Ext: " + succ.fileExt)

print("\n\n")

# Example 2 Successful parsing of file
if succ2.wasParsed:
    print("Able to parse file: " + succ2.fileName)
    print("File: " + succ2.fileName)
    print("Name: " + succ2.showName)
    print("Season: " + succ2.season)
    print("Episode: " + succ2.episode)
    print("SeasonEpisode: " + succ2.seasonEpisode)
    print("Resolution: " + succ2.getResolution())
    print("Ext: " + succ2.fileExt)
