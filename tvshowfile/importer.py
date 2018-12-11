import os

modPath = os.path.abspath(__file__)
modDirPath = os.path.dirname(modPath)


class TVShowFile:

    def __init__(self, SourceFile):
        self.SourceFile = SourceFile

        # Should import platform and determine OS to know how to handle windows
        # path
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
