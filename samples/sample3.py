#!/usr/bin/env python3

# This program demonstrate obtaining show name without year information
import sys
import json

sys.path.insert(0, "..")

from tvshowfile import parser

test_SXEX = (
"v.2009.S01E13.the.title.avi",
"Se7en.(1995).S01E01.blah.avi",
"Arrow.S01E01.blah1.avi",
"Castle.(2015).S01E01.avi",
"Castle (2015) S01x03.avi",
"Castle.2015.S01E10.avi",
"Castle.S01E22.avi",
"S.W.A.T.S01E02.720p.avi",
"S.W.A.T.S02E02E03.The.Dash.720p.avi",
"S.W.A.T.2018.S02E04.The.Dash.avi",
"S.W.A.T.(2018).S02E01.Title.720p.avi",
"Doctor Who (2005).S01E01.1080p.mp3",
"The Flash 2014 S01E03 HDTV x264-LOL[ettv].avi",
"test.avi")

for  name in test_SXEX:
    print("File: " + name)
    obj = parser.Parser(name)
    if obj.wasParsed() is True:
        print("\n    " + obj.getShowNameOnly())
        print("\n")
    else:
        print("Unable to process\n")


#testSXEX = list(test_SXEX)

#with open('test.json','w') as fhandle:
#    json.dump(testSXEX,fhandle)


#with open('test.json','r') as fhandle:
#    newList = json.load(fhandle)

#newTuple = tuple(newList)

#print(newTuple)
