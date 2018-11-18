import os
import re

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
        self.season = None
        self.episode = None
        self.seasonEpisode = None
        self.fileTags = None
        self.fileExt = None

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
        
        # https://regex101.com/r/cq8tVJ/1
        # https://regex101.com/r/cq8tVJ/2
        # https://regex101.com/r/cq8tVJ/5
        return True