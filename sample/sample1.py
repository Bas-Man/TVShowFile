#!/usr/bin/env python3

import sys
sys.path.insert(0, "..")

from tvshowfile import tvshowfile

fail = tvshowfile.Parser("test.avi")
succ = tvshowfile.Parser("test.S01E01.avi")
succ2 = tvshowfile.Parser("test.S01E01.1080p.avi")

# Example 1 testing that file was able to be parsed or not
if not fail.wasParsed():
    print("Unable to parse file: " + fail.getFilename())

# Example 1 Successful parsing of file
if succ.wasParsed:
    print("Able to parse file: " + succ.getFilename())
    print("File: " + succ.getFilename())
    print("Name: " + succ.getShowName())
    print("Season: " + succ.getSeason())
    print("Episode: " + succ.getEpisode())
    print("SeasonEpisode: " + succ.getSeasonEpisode())
    print("Quality: " + succ.getQuality())
    print("Ext: " + succ.getFileExt())

print("\n\n")

# Example 2 Successful parsing of file
if succ.wasParsed:
    print("Able to parse file: " + succ2.getFilename())
    print("File: " + succ2.getFilename())
    print("Name: " + succ2.getShowName())
    print("Season: " + succ2.getSeason())
    print("Episode: " + succ2.getEpisode())
    print("SeasonEpisode: " + succ2.getSeasonEpisode())
    print("Quality: " + succ2.getQuality())
    print("Ext: " + succ2.getFileExt())