import os
import errno
import json


class ExceptionListManager:
    '''
        This class will load and save the exceptionList. this data will be
        stored in a directory named 'data' under the tvshowfile module
        directory

        Arguments: Path (str), file (str) or fullPath
        if no arguments are provided, default values are used.
        Default path is module/data/
        Default file is exceptionlist.json

    '''

    def __init__(self, path=None, file=None, fullPath=None):
        # TODO: Handle RaisedException FileNotFoundError
        if path is None:
            self.path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
        else:
            self.path = path

        if file is None:
            self.file = "exceptionlist.json"
        else:
            self.file = file

        self.__ValidatePathFile()

    def __ValidatePathFile(self):
        '''
        '''
        if not os.path.exists(self.path):
            raise OSError(
                errno.ENOENT, os.strerror(errno.ENOENT), self.path
            )

        if not os.path.isfile(self.path + self.file):
            raise OSError(
                errno.ENOENT, os.strerror(errno.ENOENT), self.file)

    def getPath(self):
        '''
            Return the path to data directory.
            rtype: Str
        '''
        return self.path

    def getFileName(self):
        '''
            Return the name of the data file.
            rtype: Str
        '''
        return self.file

    def loadExceptionList(self):
        '''
            Load the json ExceptionList data from the json file.
            rtype: ExceptionList, which is a nested Dictionary
            returns None if loading of file fails
        '''

        try:
            with open(self.path + self.file, 'r') as fhandle:
                ExceptList = json.load(fhandle)
        except OSError:
            print("Unable to open file.")
            return None

        return ExceptList
