#!/usr/bin/env python3

# This program demonstrate obtaining show name without year information
import sys
sys.path.insert(0, "..")

from tvshowfile import parser

test1 = parser.Parser("v.2009.S01E13.the.title.avi")
test2 = parser.Parser("S.W.A.T.2018.S02E04.The.Dash.avi")
test3 = parser.Parser("Castle (2015) S02E12.avi")
test4 = parser.Parser("Castle.(2015).S02E11.avi")
test5 = parser.Parser("Doctor Who (2005).S01E01.1080p.mp3")
test6 = parser.Parser("Castle.(2015).S07E23E24.avi")

# Example 1
if test1.wasParsed:
    print("Able to parse file: " + test1.fileName)
    print("File: " + test1.fileName)
    print("Name: " + test1.showName)
    print("Name Only: " + test1.getShowNameOnly())
    print("Year: " + test1.year)
    print("Season: " + test1.season)
    print("Episode: " + test1.episode)
    print("SeasonEpisode: " + test1.seasonEpisode)
    print("Resolution: " + test1.getResolution())
    print("Ext: " + test1.fileExt)


# Example 2
if test2.wasParsed:
    print("Able to parse file: " + test2.fileName)
    print("File: " + test2.fileName)
    print("Name: " + test2.showName)
    print("Name Only: " + test2.getShowNameOnly())
    print("Year: " + test2.year)
    print("Season: " + test2.season)
    print("Episode: " + test2.episode)
    print("SeasonEpisode: " + test2.seasonEpisode)
    print("Resolution: " + test2.getResolution())
    print("Ext: " + test2.fileExt)

# Example 3
if test3.wasParsed:
    print("Able to parse file: " + test3.fileName)
    print("File: " + test3.fileName)
    print("Name: " + test3.showName)
    print("Name Only: " + test3.getShowNameOnly())
    print("Year: " + test3.year)
    print("Season: " + test3.season)
    print("Episode: " + test3.episode)
    print("SeasonEpisode: " + test3.seasonEpisode)
    print("Resolution: " + test3.getResolution())
    print("Ext: " + test3.fileExt)

# Example 4
if test4.wasParsed:
    print("Able to parse file: " + test4.fileName)
    print("File: " + test4.fileName)
    print("Name: " + test4.showName)
    print("Name Only: " + test4.getShowNameOnly())
    print("Year: " + test4.year)
    print("Season: " + test4.season)
    print("Episode: " + test4.episode)
    print("SeasonEpisode: " + test4.seasonEpisode)
    print("Resolution: " + test4.getResolution())
    print("Ext: " + test4.fileExt)

# Example 5
if test5.wasParsed:
    print("Able to parse file: " + test5.fileName)
    print("File: " + test5.fileName)
    print("Name: " + test5.showName)
    print("Name Only: " + test5.getShowNameOnly())
    print("Year: " + test5.year)
    print("Season: " + test5.season)
    print("Episode: " + test5.episode)
    print("SeasonEpisode: " + test5.seasonEpisode)
    print("Resolution: " + test5.getResolution())
    print("Ext: " + test5.fileExt)

# Example 6
if test6.wasParsed:
    print("Able to parse file: " + test6.fileName)
    print("File: " + test6.fileName)
    print("Name: " + test6.showName)
    print("Name Only: " + test6.getShowNameOnly())
    print("Year: " + test6.year)
    print("Season: " + test6.season)
    if test6.isMultiEpisode:
        print("First Episode: " + test6.getFirstEpisode())
        print("Last Episode: " + test6.getLastEpisode())
    else:
        print("Episode: " + test6.episode)
    print("SeasonEpisode: " + test6.seasonEpisode)
    print("Resolution: " + test6.getResolution())
    print("Ext: " + test6.fileExt)
