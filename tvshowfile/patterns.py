
patterns =[
    r"""
	(?P<ShowNameA>.*)(?=(?:[. ](?:[S][0-9]{2})|[0-9][x])) #Show name
	(?: # Get year if present
	[ .]?(?<=[.( ](?P<Year>\d{4})[.) ])
	| # Get Season
	[. ](?:S(?P<ShowSeason>\d{1,2}))[E|X]
	)
	(?: # Get Episodes in case multi episode file
	(?P<FirstEpisode>[0-9]{1,2})(?:[E])(?P<LastEpisode>[0-9]{1,2})
	| # Get single Eposide if single episode
	(?P<Episode>[0-9]{1,2})
	)
	[.] # Finished getting Seasons and Episodes
	(?:.*) # Get everything else but not the file extension
	[.]?(?<=(?P<FileExt>[a-z]{3}|[a-z]{2}[0-9]{1}) # Get the file extension
	)
	"""
 ]

