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
        test1.year,
        test1.seasonEpisode,
        test1.fileExt
    )
    print("Old File: " + test1.fileName + "; New File: " + newFileName)

# Example 2
if test2.wasParsed:
    # Start building to filename
    newFileName = "{}.({}).{}.{}".format(
        test2.getShowNameOnly(),
        test2.year,
        test2.seasonEpisode,
        test2.fileExt
    )
    print("Old File: " + test2.fileName + "; New File: " + newFileName)

# Example 3
if test3.wasParsed:
    # Start building to filename
    newFileName = "{}.({}).{}.{}".format(
        test3.getShowNameOnly(),
        test3.year,
        test3.seasonEpisode,
        test3.fileExt
    )
    print("Old File: " + test3.fileName + "; New File: " + newFileName)
