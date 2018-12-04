import os
import re
import datetime

from .patterns import regex_SXEX, regex_name_only, regex_YEAR, regex_quality

# This may be used to store exception show names in the module directory
# This will help keep things clean.
modPath = os.path.abspath(__file__)
modDirPath = os.path.dirname(modPath)

class Parser:

    '''
        This object has the responsibility of collecting information from the
        file name of a TV show DVD rip or other digital source
        Give a filename such as "Castle.2009.S01E01.avi" it will identify and
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
    def __init__(self,filename):
        self.filename = filename
        self.showName = None
        self.showNameOnly = None
        self.year = None
        self.season = None
        self.episode = None
        self.seasonEpisode = None
        self.firstEpisode = None
        self.lastEpisode = None
        self.quality = None
        self.fileExt = None
        self.multiEpisode = False
        self.Parsed = False

        # Failed to get any input
        if not filename:
            return None
        else:
            self.getShowData()

    # Object Destructor
    def __del__(self):
        pass

    # Parse show filename and store required information in object
    # attributes
    def getShowData(self):
        '''
        Parse show filename and store required information in object
        attributes

        # Reference code https://github.com/ROldford/tvregex
        # Reference code https://github.com/dbr/tvnamer
        # Reference code https://github.com/ghickman/tvrenamr

        # https://regex101.com/r/cq8tVJ/10

        # My Patterns
        # Possible starting places
        # https://regex101.com/r/mS4a2A/9/
        # https://regex101.com/r/8AJ8Lg/4/ #Possible Option
        # https://regex101.com/r/iqxoAB/2 # Name only omitting Year if presents
        '''

        pattern = re.compile(regex_SXEX, re.IGNORECASE | re.VERBOSE)
        match = pattern.match(self.filename)

        # TODO: This should be changed at some point to support multiple
        # regex patterns
        
        if match:
            self._patternSXEX(match)
            self.Parsed = True
            return True
        else:
            self.Parsed = False
            return False

    def _patternSXEX(self,match):
        '''
            This is an internal function and should not need to be called.
            It is called by __init__
            It should match file names with Series and Episodes in the form
            of SXXEXX  or SXXEXXEXX (Multi-Episode)

            This method as no return type SEE method 'wasParsed'
        '''

        '''
            showName, season, and fileExt are expected to match as a minimum
            EXX and EXXEXX are matched conditionally
            Year of first Episode and resolution are looked for but not assumed
            to be present
        '''
        self.showName = match.group("showname")
        self.season = match.group("showseason")
        self.fileExt = match.group("fileext")

        # Optional Values
        # Multi Episode file
        if match.group("firstepisode"):
            self.firstEpisode = match.group("firstepisode")
            self.lastEpisode = match.group("lastepisode")
            # Build Season and Mulit Episode String
            self.seasonEpisode = "S{0}E{1}E{2}".format(
                self.season,self.firstEpisode,self.lastEpisode
                )
            # Set multiEpisode to True
            self.multiEpisode = True
        # Single Episode file
        else:
            self.episode = match.group("episode")
            # Build Season and single Episode String
            self.seasonEpisode = "S{0}E{1}".format(self.season,self.episode)
        # File contains a Year
        self._patternYear()
        # File contains Quality
        self._getQuality()

    def _patternYear(self):

        '''
            This method should not need to be called by code it will be called
            by _pattern* internal methods
            Get Year if it exists. We have to search the string since we do not
            have a full string match regex
        '''

        pattern = re.compile(regex_YEAR, re.IGNORECASE | re.VERBOSE)
        match = pattern.search(self.filename)

        if match:
            # Check that matched year string is between 1920 and the current year
            # If this is not true, then we have probably matched a show name like "The 4400"
            if(1920 <= int(match.group("year")) <= datetime.datetime.now().year):
                self.year = match.group("year")

    def _getQuality(self):
        '''
            This method should not need to be called by code it will be called
            by _pattern* internal methods
            Get video quality if listed in the file name
            This currently only supports 720p or 1080p
        '''
        #TODO: Update pattern to also support SD values. Need to find examples

        pattern = re.compile(regex_quality, re.IGNORECASE | re.VERBOSE)
        match = pattern.search(self.filename)

        if match:
            self.quality = match.group("quality")

    def getFilename(self):
        '''
            Get the string held in filename. The full name of the file being
            processed

            Returns a Str
        '''
        return self.filename

    def getShowName(self):
        '''
            Get the string held in showName. This is unprocessed so will contain
            any characthers like . - or others which separate words in the name

            Returns a Str
        '''
        return self.showName

    def getSeason(self):
        '''
            Get the string held in Season.
            This will be a number only without the "S"

            Returns a Str
        '''
        return self.season

    def getEpisode(self):
        '''
            Get the string held in episode. This will be empty if
            isMultiEpisode is True. This will be a number only without the "E"

            Returns a Str
        '''
        # If this is True then episode will still be None.
        # We should return an empty string
        if self.isMultiEpisode():
            return ""
        return self.episode

    def getSeasonEpisode(self):
        '''
            Get the string held in seasonEpisode This will be in the form of
            SXXEXX or SXXEXXEXX

            Returns a Str
        '''
        return self.seasonEpisode

    def getFileExt(self):
        '''
            Get the string held in fileExt should be avi mp3 srt or such
        '''
        return self.fileExt

    def getFirstEpisode(self):
        '''
            Get the string held in firstEpisode. This will only exist
            if isMultiEpisode is True

            You should check if isMultiEpisode is True before calling this
            method
            Returns a Str
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
            Returns a Str
        '''
        if self.lastEpisode is not None:
            return self.lastEpisode
        else:
            return ""

    def getYear(self):
        '''
            Get the string held in attribute year
            Returns a Str. This will be "" if there is no year was found in the
            filename
        '''
        if self.year is not None:
            return self.year
        else:
            return ""

    def getQuality(self):
        '''
            Get the string held in attribute quality

            Returns a Str. This will be an empty string if no quality was found
            This will be something like 720p or 1080p
        '''
        if self.quality is not None:
            return self.quality
        else:
            return ""

    def hasYear(self):
        '''
            Check that Filename had a Year used before calling getYear

            Returns True or False
        '''
        if self.year is not None:
            return True
        return False

    def isMultiEpisode(self):
        '''
            Check if the file contains more than one episode.
            This is needed when working with firstEpisode and lastEpisode

            This method should be called so you know if you should call
            getEpisode() or getFirstEpisode() and getLastEpisode()

            Returns True or False
        '''
        if self.multiEpisode:
            return True
        return False

    # Check if filename contains a quality string like 720p
    def hasQaulity(self):
        '''
            Check if filename contains a quality string like 720p

            Returns True or False
        '''
        if self.quality is not None:
            return True
        return False

    # Return True or False if the file was able to be parsed.
    def wasParsed(self):
        '''
            Return True or False if the file was able to be parsed.

            if obj.wasParsed:
                # Do some work
            else:
                # move to next
        '''
        return self.Parsed

    def getShowNameOnly(self):
        '''
            Return the show name without year if it exists

            Returns a Str
        '''
        #TODO: This may need to be changed to handle show names that have four
        #digits in their names
        #TODO: Example "The 4400"
        if self.showNameOnly is not None:
            # This has been called before, simply returned stored value
            return self.showNameOnly
        else:
            # We need to parse, set and return. This function has not previously
            # been called
            pattern = re.compile(regex_name_only, re.IGNORECASE | re.VERBOSE)
            match = pattern.match(self.filename)

            if match:
                # This pattern contains 6 groups. group(0), group(3) and
                #group(6) are of no interest.
                # So we restrict to 1,2,4,5 skip 3 using a continue statement
                for groupNum in range(0, len(match.groups()) - 1):
                    groupNum = groupNum + 1 # skip group(0) by incrementing at
                    #the start of the loop
                    if groupNum == 3: #Skip group(3)
                        continue
                    if match.group(groupNum) is not None: # This group has a
                    #match we can use it and break from loop
                        self.showNameOnly = match.group(groupNum)
                        break

                return self.showNameOnly
            else:
                self.showNameOnly = ""
                return ""

    def loadExceptionList(self):
        '''
            This method loads a list of show names which are exceptions that
            need
            be handled differently. Examples S.W.A.T and The 4400

        '''
        pass

    def writeExceptionList(self):
        '''
            This method write the contents of the exception list to file

        '''
        pass

    def appendShowNameException(self):
        '''
            This method appends a new show name exception to the ExceptionList
        '''
        pass
