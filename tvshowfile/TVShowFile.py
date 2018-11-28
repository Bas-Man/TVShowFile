import os
import re
from .patterns import regex_SXEX, regex_YEAR, regex_quality

class TVShowFile:

    def __init__(self,SourceFile):
        self.SourceFile = SourceFile

        # Should import platform and determine OS to know how to handle windows path
        # if windows should import ntpath and use ntpath.split()
        # see https://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python
        # More reading required to know if this is actually needed.
        self.absPath, self.filename = os.path.split(SourceFile)

    def folderExists(self):
        return os.path.isdir(self.absPath)

    def fileExists(self):
        # Return
        return os.path.exists(self.SourceFile)

    def FilePath(self):
        return self.SourceFile

class TVShowFileParser:

    # Object Constructor
    def __init__(self,filename):
        self.filename = filename
        self.showName = None
        self.year = None
        self.season = None
        self.episode = None
        self.seasonEpisode = None
        self.firstEpisode = None
        self.lastEpisode = None
        self.quality = None
        self.fileExt = None
        self.multiEpisode = False

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
        # Reference code https://github.com/ROldford/tvregex
        # Reference code https://github.com/dbr/tvnamer
        # Reference code https://github.com/ghickman/tvrenamr


        # https://regex101.com/r/cq8tVJ/10
        
        # My Patterns
        # Possible starting places
        # https://regex101.com/r/mS4a2A/9/
        # https://regex101.com/r/8AJ8Lg/4/ #Possible Option
        pattern = re.compile(regex_SXEX, re.IGNORECASE | re.VERBOSE)

        match = pattern.match(self.filename)
        
        if match:
            self._patternSXEX(match)
            return True
        else:
            return False
      
    def _patternSXEX(self,match):
        # These values must exist if there is a match
        self.showName = match.group("showname")
        self.season = match.group("showseason")
        self.fileExt = match.group("fileext")
        
        # Optional Values
        # Multi Episode file
        if match.group("firstepisode"):
            self.firstEpisode = match.group("firstepisode")
            self.lastEpisode = match.group("lastepisode")
            self.seasonEpisode = "S" + self.season + "E" + self.firstEpisode + "E" + self.lastEpisode
            # Set multiEpisode to True
            self.multiEpisode = True
        # Single Episode file
        else:
            self.episode = match.group("episode")
            self.seasonEpisode = "S" + self.season + "E" + self.episode
        
        # File contains a Year
        self._patternYear()
        # File contains Quality
        self._getQuality()

    def _patternYear(self):

        # Get Year if it exists. We have to search the string since we do not have a full string match regex
        pattern = re.compile(regex_YEAR, re.IGNORECASE | re.VERBOSE)
        match = pattern.search(self.filename)

        if match:
            self.year = match.group("year")

    def _getQuality(self):

        # Get video quality if listed in the file name
        pattern = re.compile(regex_quality, re.IGNORECASE | re.VERBOSE)
        match = pattern.search(self.filename)

        if match:
            self.quality = match.group("quality")


    def getShowName(self):
        return self.showName

    def getSeason(self):
        return self.season

    def getEpisode(self):
        return self.episode

    def getSeasonEpisode(self):
        return self.seasonEpisode

    def getFileExt(self):
        return self.fileExt

    def getFirstEpisode(self):
        if self.firstEpisode is not None:
            return self.firstEpisode
        else:
            return ""

    def getLastEpisode(self):
        if self.lastEpisode is not None:
            return self.lastEpisode
        else:
            return ""

    def getYear(self):
        if self.year is not None:
            return self.year
        else:
            return ""

    def getQuality(self):
        if self.quality is not None:
            return self.quality
        else:
            return ""
            
    # Check that Filename had a Year used before calling getYear
    def hasYear(self):
        if self.year is not None:
            return True
        return False

    def isMultiEpisode(self):
        if self.multiEpisode:
            return True
        return False
