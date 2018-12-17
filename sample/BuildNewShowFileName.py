#!/usr/bin/env python3

# This program demonstraties how one might reconstruct a filename
import sys
sys.path.insert(0, "..")
from tvshowfile import parser

test1 = parser.Parser("v.2009.S01E13.the.title.avi")
test2 = parser.Parser("S.W.A.T.2018.S02E04.The.Dash.avi")
test3 = parser.Parser("Castle (2015) S02E12.avi")

# Example 1
if test1.wasParsed:
    # Start building to filename
    newFileName = "{}.({}).{}.{}".format(
        test1.getShowNameOnly().capitalize(),
        test1.getYear(),
        test1.getSeasonEpisode(),
        test1.getFileExt()
    )
    print("Old File: " + test1.filename + "; New File: " + newFileName)

# Example 2
if test2.wasParsed:
    # Start building to filename
    newFileName = "{}.({}).{}.{}".format(
        test2.getShowNameOnly(),
        test2.getYear(),
        test2.getSeasonEpisode(),
        test2.getFileExt()
    )
    print("Old File: " + test2.filename + "; New File: " + newFileName)

# Example 3
if test3.wasParsed:
    # Start building to filename
    newFileName = "{}.({}).{}.{}".format(
        test3.getShowNameOnly(),
        test3.getYear(),
        test3.getSeasonEpisode(),
        test3.getFileExt()
    )
    print("Old File: " + test3.filename + "; New File: " + newFileName)
