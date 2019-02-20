import os
import re
import datetime

from .patterns import regex_SXEX, regex_bydate, regex_name_only
from .patterns import regex_YEAR, regex_resolution
from .patterns import listOfSubExts, regex_subtitle, regex_ripper
from .exceptman import ExceptionListManager

# This may be used to store exception show names in the module directory
# This will help keep things clean.
modDirPath = os.path.dirname(os.path.abspath(__file__))


class Parser:
    # Class Attributes
    ExMan = None

    '''
        This object has the responsibility of collecting information from the
        file name of a TV show DVD rip or other digital source.
        Given a filename such as "Castle.2009.S01E01.avi" it will identify and
        store the following elements
        The object will be populated using __init__

        + filename
        + showName Castle.2009
        + showNameOnly Castle
        + year 2009
        + season 01
        + episode 01
        + seasonEpisode S01E01
        + fileExt avi

    '''

    # Object Constructor
    def __init__(self, filename):
        self._fileName = filename
        self._showName = None
        self._showNameOnly = None
        self._year = None
        self._month = None
        self._date = None
        self._season = None
        self._episode = None
        self._seasonEpisode = None
        self.firstEpisode = None
        self.lastEpisode = None
        self._resolution = None
        self._fileExt = None
        self._multiEpisode = False
        self._parsed = False
        self._lang = None
        self._ripper = None

        # Failed to get any input
        if not filename:
            return None
        else:
            # Load the ExceptionList data Exman and ExceptionList are Global
            # This should only need to be loaded once

            if Parser.ExMan is None:
                Parser.ExMan = ExceptionListManager()
                Parser.ExMan.loadExceptionList()

            self.getShowData()

    # Object Destructor
    def __del__(self):
        pass

    def getShowData(self):
        '''
        Parse show filename and store required information in object
        attributes

        rtype: Bool
        '''
        if self._patternSXEX():     # Match was found and file parsed
            return True
        elif self._patternByDate():  # Match was found and file was parsed
            return True
        else:   # No Match found and we could not parse the filename
            return False

    def _patternByDate(self):
        '''
            This is an internal function and should not need to be called.
            It is called by __init__
            It should match file names like Jimmy.Fallon.2019.01.29*.mkv

            rtype Bool
        '''

        pattern = re.compile(regex_bydate, re.IGNORECASE | re.VERBOSE)
        match = pattern.match(self._fileName)

        if match:
            self._showName = match.group("showname")
            self._year = match.group("year")
            self._month = match.group("month")
            self._date = match.group("date")
            self._fileExt = match.group("fileext")
            self._parsed = True
            return True
        else:
            return False

    def _patternSXEX(self):
        '''
            This is an internal function and should not need to be called.
            It is called by __init__
            It should match file names with Series and Episodes in the form
            of SXXEXX  or SXXEXXEXX (Multi-Episode)

            rtype Bool
        '''

        # showName, season, and fileExt are expected to match as a minimum
        # EXX and EXXEXX are matched conditionally
        # Year of first Episode and resolution are looked for but not assumed
        # to be present

        pattern = re.compile(regex_SXEX, re.IGNORECASE | re.VERBOSE)
        match = pattern.match(self._fileName)

        if match:
            self._showName = match.group("showname")
            self._season = match.group("showseason")
            self._fileExt = match.group("fileext")

            # Optional Values
            # Multi Episode file
            if match.group("firstepisode"):
                self.firstEpisode = match.group("firstepisode")
                self.lastEpisode = match.group("lastepisode")
                # Build Season and Mulit Episode String
                self._seasonEpisode = "S{0}E{1}E{2}".format(
                    self._season, self.firstEpisode, self.lastEpisode
                    )
                # Set multiEpisode to True
                self._multiEpisode = True
            # Single Episode file
            else:
                self._episode = match.group("episode")
                # Build Season and single Episode String
                self._seasonEpisode = "S{0}E{1}".format(self._season,
                                                        self._episode)
            # File contains a Year
            self._patternYear()
            # File contains resolution
            self._getResolution()
            self._parsed = True
            return True
        else:
            return False

    def _patternYear(self):
        '''
            This method should not need to be called by code it will be called
            by _pattern* internal methods
            Get Year if it exists. We have to search the string since we do not
            have a full string match regex
        '''

        pattern = re.compile(regex_YEAR, re.IGNORECASE | re.VERBOSE)
        match = pattern.search(self._fileName)

        if match:
            # Check that matched year string is between 1920 and the current
            # year
            # If this is not true, then we have probably matched a show name
            # like "The 4400"
            if(1920 <= int(match.group("year"))
               <= datetime.datetime.now().year):
                self._year = match.group("year")

    def _getResolution(self):
        '''
            This method should not need to be called by code it will be called
            by _pattern* internal methods
            Get video resolution if listed in the file name
            This currently only supports 720p or 1080p
        '''

        # TODO: Update pattern to also support SD values. Need to find examples

        pattern = re.compile(regex_resolution, re.IGNORECASE | re.VERBOSE)
        match = pattern.search(self._fileName)

        if match:
            self._resolution = match.group("resolution")

    @property
    def fileName(self):
        '''
            Get the string held in filename. The full name of the file being
            processed

            trype: Str
        '''
        return self._fileName

    @property
    def showName(self):
        '''
            Get the string held in showName. This is unprocessed so will
            contain any characthers like . - or others which separate words in
            the name

            rtype: Str
        '''
        return self._showName

    @property
    def season(self):
        '''
            Get the string held in Season.
            This will be a number only without the "S"

            rtype: Str
        '''
        return self._season

    @property
    def episode(self):
        '''
            Get the string held in episode. This will be empty if
            isMultiEpisode is True. This will be a number only without the "E"

            rtype: Str
        '''
        # If this is True then episode will still be None.
        # We should return an empty string
        if self.isMultiEpisode:
            return ""
        return self._episode

    @property
    def seasonEpisode(self):
        '''
            Get the string held in seasonEpisode This will be in the form of
            SXXEXX or SXXEXXEXX

            rtype: Str
        '''
        return self._seasonEpisode

    @property
    def fileExt(self):
        '''
            Get the string held in fileExt should be avi mp3 srt or such
            rtype: Str
        '''
        return self._fileExt

    def getFirstEpisode(self):
        '''
            Get the string held in firstEpisode. This will only exist
            if isMultiEpisode is True

            You should check if isMultiEpisode is True before calling this
            method
            rtype: Str
        '''
        if self.firstEpisode is not None:
            return self.firstEpisode
        else:
            return ""

    def getLastEpisode(self):
        '''
            Get the string held in lastEpisode. This will only exist
            if isMultiEpisode is True

            You should check if isMultiEpisode is True before calling this
            method
            rtype: Str
        '''
        if self.lastEpisode is not None:
            return self.lastEpisode
        else:
            return ""

    @property
    def year(self):
        '''
            Get the string held in attribute year
            Returns a Str. This will be "" if there is no year was found in the
            filename
            rtype: Str
        '''
        if self._year is not None:
            return self._year
        else:
            return ""

    @property
    def month(self):
        '''
            Get the string held in attribute month
            Returns a Str. This will be "" if there is no month was found in
            the filename
            rtype: Str
        '''
        if self._month is not None:
            return self._month
        else:
            return ""

    @property
    def date(self):
        '''
            Get the string held in attribute date
            Returns a Str. This will be "" if there is no date was found in the
            filename
            rtype: Str
        '''
        if self._date is not None:
            return self._date
        else:
            return ""

    @property
    def resolution(self):
        '''
            Get the string held in attribute resolution

            This will be an empty string if no resolution was
            found
            This will be something like 720p or 1080p
            rtype: Str
        '''
        if self._resolution is not None:
            return self._resolution
        else:
            return ""

    @property
    def hasYear(self):
        '''
            Check that Filename had a Year used before calling getYear

            rtype: Bool
        '''
        if self._year is not None:
            return True
        return False

    @property
    def isMultiEpisode(self):
        '''
            Check if the file contains more than one episode.
            This is needed when working with firstEpisode and lastEpisode

            This method should be called so you know if you should call
            getEpisode() or getFirstEpisode() and getLastEpisode()

            rtype: Bool
        '''
        if self._multiEpisode:
            return True
        return False

    @property
    def hasResolution(self):
        '''
            Check if filename contains a resolution string like 720p

            rtype: Bool
        '''
        if self._resolution is not None:
            return True
        return False

    @property
    def wasParsed(self):
        '''
            rtype: Bool

            if obj.wasParsed:
                # Do some work
            else:
                # move to next
        '''
        return self._parsed

    @property
    def showNameOnly(self):
        '''
            Return the show name without year if it exists

            Returns a Str
        '''
        # TODO: This may need to be changed to handle show names that have four
        # digits in their names
        # TODO: Example "The 4400"
        if self._showNameOnly is not None:
            # This has been called before, simply return stored value
            return self._showNameOnly
        else:

         # if showNameIsAnException is true then the name is complete already
         # We will use it as is without trying to re-parse the name.
         # This does short circuit the logic so the "if match:" does not
         # happen

            if self.showNameIsAnException():
                self._showNameOnly = self._showName
                return self._showNameOnly
            # We need to parse, set and return. This function has not
            # previously been called
            pattern = re.compile(regex_name_only, re.IGNORECASE | re.VERBOSE)
            match = pattern.match(self._fileName)

            if match:
                # This pattern contains 6 groups. group(0), group(3) and
                # group(6) are of no interest.
                # So we restrict to 1,2,4,5 skip 3 using a continue statement
                for groupNum in range(0, len(match.groups()) - 1):
                    # skip group(0) by incrementing at the start of the loop
                    groupNum = groupNum + 1
                    if groupNum == 3:  # Skip group(3)
                        continue
                    if match.group(groupNum) is not None:
                        # This group has a match we can use it and break
                        # from loop
                        self._showNameOnly = match.group(groupNum)
                        break
                return self._showNameOnly
            else:
                self._showNameOnly = ""
                return ""

    def showNameIsAnException(self):
        '''
            Using nested Dictionaries. This checks that there is an initial
            Key in the ExceptionList

            rtype: Bool
        '''
        if Parser.ExMan.hasKey(self._showName.lower()):
            return True
        else:
            return False

    def _showNameKeepsPeriods(self):
        '''
            Internal method to check if the show name should keep its periods
            Example S.W.A.T
            rtype: Bool
        '''
        return Parser.ExMan.keepsPeriods(self.showNameOnly)

    def _getShowNameFromExceptionList(self):
        '''
            Internal method this returns the value from key: name or None if
            if key is not found

            rtype:  Str
        '''
        return Parser.ExMan.getShowNameByKey(self.showName)

    def _showNameIsAnException(self):
        '''
            Internal method to check if show name is in our ExceptionList
            rtype: Bool
        '''
        return Parser.ExMan.hasKey(self.showNameOnly)

    def getCleanShowName(self):
        '''
            This method will return a clean show name without periods
            the.4400 -> the 4400
            Using an internal ExceptionList however periods will not be removed
            for show names like s.w.a.t

            rtype: Str
        '''
        # Check if in exceptionList and if has name key, return name else ...
        if self._showNameIsAnException() \
           and self._getShowNameFromExceptionList() is not None:
                return self._getShowNameFromExceptionList()
        # Check if key exists and if keepPeriods is True or False
        # if keepPeriods is True just return showNameOnly
        elif self._showNameIsAnException() and self._showNameKeepsPeriods():
            return self.showNameOnly
        # keepPeriods is False so we want to remove any periods in the
        # showNameOnly()
        else:
            return self.showNameOnly.replace('.', ' ')

    @property
    def isSubs(self):
        '''
            Allows user to check if the file a subtitle file based on extension
            Currently supports srt, smi, ass, ssa, and TVShowFileParserTests

            rtype: Bool
        '''
        if self.fileExt in listOfSubExts:
            return True
        else:
            return False

    @property
    def subLanguage(self):
        '''
            returns the language given in the filename. E.G en.srt will
            return en
            rtype: Str
        '''
        if self._lang is not None:
            return self._lang
        else:
            pattern = re.compile(regex_subtitle, re.IGNORECASE | re.VERBOSE)
            match = pattern.search(self._fileName)

            if match:
                self._lang = match.group('lang')
            else:
                self._lang = ""

            return self._lang

    @property
    def ripper(self):
        '''
            Return the group that created the rip if present in the file.
            rtype: Str
        '''
        if self._ripper is not None:
            return self._ripper
        else:
            pattern = re.compile(regex_ripper, re.IGNORECASE | re.VERBOSE)
            match = pattern.search(self._fileName)

            if match:
                self._ripper = match.group('ripper')
            else:
                self._ripper = ""

            return self._ripper
