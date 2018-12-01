#!/usr/bin/env python3

# This program demonstraties how one might reconstruct a filename
import sys
sys.path.insert(0, "..")

from tvshowfile import tvshowfile

test1 = tvshowfile.Parser("v.2009.S01E13.the.title.avi")
test2 = tvshowfile.Parser("S.W.A.T.2018.S02E04.The.Dash.avi")
test3 = tvshowfile.Parser("Castle (2015) S02E12.avi")

# Example 1 
if test1.wasParsed:
    #Start building to filename
    newFileName = test1.getShowNameOnly().capitalize()
    newFileName +=  ".(" + test1.getYear()
    newFileName += ")."
    newFileName += test1.getSeasonEpisode() + "."
    newFileName += test1.getFileExt()
    print("New File: " + newFileName)

# Example 2 
if test2.wasParsed:
    #Start building to filename
    newFileName = test2.getShowNameOnly()
    newFileName +=  ".(" + test2.getYear()
    newFileName += ")."
    newFileName += test2.getSeasonEpisode() + "."
    newFileName += test2.getFileExt()
    print("New File: " + newFileName)

# Example 3 
if test3.wasParsed:
    #Start building to filename
    newFileName = test3.getShowNameOnly()
    newFileName +=  ".(" + test3.getYear()
    newFileName += ")."
    newFileName += test3.getSeasonEpisode() + "."
    newFileName += test3.getFileExt()
    print("New File: " + newFileName)