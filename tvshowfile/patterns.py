
# coding=utf8

regex_SXEX = r"""
(?P<showname>.*)(?=(?:[. ](?:[S][0-9]{2})|[0-9][x])) #Show name
(?: # Get year if present
[ .]?(?<=[.( ](?P<showyear>\d{4})[.) ])
| # Get Season
[. ](?:S(?P<showseason>\d{1,2}))[E|X]
)
(?: # Get Episodes in case multi episode file
(?P<firstepisode>[0-9]{1,2})(?:[E])(?P<lastepisode>[0-9]{1,2})
| # Get single Eposide if single episode
(?P<episode>[0-9]{1,2})
)
[.]? # Finished getting Seasons and Episodes
(?:.*) # Get everything else but not the file extension
[.]?(?<=(?P<fileext>[a-z]{3}|[a-z]{2}[0-9]{1}) # Get the file extension
)
"""

test_SXEX = ("v.2009.S01E13.the.title.avi\n"
"Se7en.(1995).S01E01.blah.avi\n"
"Arrow.S01E01.blah1.avi\n"
"Castle.(2015).S01E01.avi\n"
"Castle (2015) S01x03.avi\n"
"Castle.2015.S01E10.avi\n"
"Castle.S01E22.avi\n"
"Castle.(2015).S02E11.avi\n"
"Castle (2015) S02E12.avi\n"
"S.W.A.T.S01E02.720p.avi\n"
"S.W.A.T.S02E02E03.The.Dash.720p.avi\n"
"S.W.A.T.2018.S02E04.The.Dash.avi\n"
"S.W.A.T.(2018).S02E01.Title.720p.avi\n"
"Doctor Who (2005).S01E01.1080p.mp3\n"
"The Flash 2014 S01E03 HDTV x264-LOL[ettv].avi")

regex_title_year = r"""
	(?P<ShowName>.*)(?=(?:[. ](?:[S][0-9]{2})|[s][0-9][x])) #Show name
	(?: # Get year if present
	[ .]?(?<=(?P<Year>[.(]\d{4}[).]))
	| # Blank alternate required
	)
	"""

regex_name_only = r"""
	(?P<Title1>.*)\s\(\d{4}
	|
	(?P<Title2>.*)(^[.]\d{4})
	|
	(?P<Title3>.*)[. ]\(
	|
	(?P<Title4>.*[^\d)])[. ]+(\d{4}|S).*
	"""
	
regex_YEAR = r"""
	(?P<year>\d{4})[ ).S]+
	"""
	
regex_quality = r"""
	(?P<quality>[0-9]{3,4}[p|i])
	"""