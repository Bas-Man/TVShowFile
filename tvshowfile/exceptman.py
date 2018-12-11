import os
import json


class ExceptionListManager:
    '''
        This class will load and save the exceptionList. this data will be
        stored in a directory named 'data' under the tvshowfile module
        directory

    '''

    def __init__(self, path=None, file=None):
        # TODO: Handle RaisedException FileNotFoundError
        if path is None:
            self.path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
        else:
            self.path = path

        if file is None:
            self.file = "exceptionlist.json"
        else:
            self.file = file

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
        '''

        with open(self.path + self.file, 'r') as fhandle:
            ExceptList = json.load(fhandle)

        return ExceptList
