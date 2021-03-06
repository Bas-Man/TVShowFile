
# coding=utf8

# TODO: Move regex patterns into a dict for easier handling?

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

regex_bydate = r"""
(?P<showname>.*)[.] #Show Name
(?P<year>\d{4})[.] #Show Year
(?P<month>\d{2})[.] # Month
(?P<date>\d{2})[.]
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

regex_resolution = r"""
(?P<resolution>[0-9]{3,4}[p|i])
"""

regex_subtitle = r"""
(?P<lang>[a-z]{2,})[.](?P<subsext>srt|smi|ssa|ass|vtt)$
"""

# List of Subtitle extensions for checking
listOfSubExts = ['srt', 'smi', 'ssa', 'ass', 'vtt']

#  [\[] the \ is used as python gives a FutureWarning without it.
#  It appears we need to escape the second [ character in the class specifier
regex_ripper = r"""
[\[]?(?P<ripper>fov|vtv|ettv|rmteam|eztv)[]]?
"""
