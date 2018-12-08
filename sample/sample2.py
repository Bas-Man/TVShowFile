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

# Example 1
if test1.wasParsed:
    print("Able to parse file: " + test1.getFilename())
    print("File: " + test1.getFilename())
    print("Name: " + test1.getShowName())
    print("Name Only: " + test1.getShowNameOnly())
    print("Year: " + test1.getYear())
    print("Season: " + test1.getSeason())
    print("Episode: " + test1.getEpisode())
    print("SeasonEpisode: " + test1.getSeasonEpisode())
    print("Resolution: " + test1.getResolution())
    print("Ext: " + test1.getFileExt())


# Example 2
if test2.wasParsed:
    print("Able to parse file: " + test2.getFilename())
    print("File: " + test2.getFilename())
    print("Name: " + test2.getShowName())
    print("Name Only: " + test2.getShowNameOnly())
    print("Year: " + test2.getYear())
    print("Season: " + test2.getSeason())
    print("Episode: " + test2.getEpisode())
    print("SeasonEpisode: " + test2.getSeasonEpisode())
    print("Resolution: " + test2.getResolution())
    print("Ext: " + test2.getFileExt())

# Example 3
if test3.wasParsed:
    print("Able to parse file: " + test3.getFilename())
    print("File: " + test3.getFilename())
    print("Name: " + test3.getShowName())
    print("Name Only: " + test3.getShowNameOnly())
    print("Year: " + test3.getYear())
    print("Season: " + test3.getSeason())
    print("Episode: " + test3.getEpisode())
    print("SeasonEpisode: " + test3.getSeasonEpisode())
    print("Resolution: " + test3.getResolution())
    print("Ext: " + test3.getFileExt())

# Example 4
if test4.wasParsed:
    print("Able to parse file: " + test4.getFilename())
    print("File: " + test4.getFilename())
    print("Name: " + test4.getShowName())
    print("Name Only: " + test4.getShowNameOnly())
    print("Year: " + test4.getYear())
    print("Season: " + test4.getSeason())
    print("Episode: " + test4.getEpisode())
    print("SeasonEpisode: " + test4.getSeasonEpisode())
    print("Resolution: " + test4.getResolution())
    print("Ext: " + test4.getFileExt())

# Example 5
if test5.wasParsed:
    print("Able to parse file: " + test5.getFilename())
    print("File: " + test5.getFilename())
    print("Name: " + test5.getShowName())
    print("Name Only: " + test5.getShowNameOnly())
    print("Year: " + test5.getYear())
    print("Season: " + test5.getSeason())
    print("Episode: " + test5.getEpisode())
    print("SeasonEpisode: " + test5.getSeasonEpisode())
    print("Resolution: " + test5.getResolution())
    print("Ext: " + test5.getFileExt())
