
# coding=utf8

#TODO: Move regex patterns into a dict for easier handling?

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

regex_title_year = r"""
	(?P<ShowName>.*)(?=(?:[. ](?:[S][0-9]{2})|[s][0-9][x])) #Show name
	(?: # Get year if present
	[ .]?(?<=(?P<Year>[.(]\d{4}[).]))
	| # Blank alternate required
	)
	"""

regex_name_only = r"""
	(?P<title1>.*)\s\(\d{4}
	|
	(?P<title2>.*)(^[.]\d{4})
	|
	(?P<title3>.*)[. ]\(
	|
	(?P<title4>.*[^\d)])[. ]+(\d{4}|S).*
	"""

regex_YEAR = r"""
	(?P<year>\d{4})[ ).S]+
	"""

regex_quality = r"""
	(?P<quality>[0-9]{3,4}[p|i])
	"""
