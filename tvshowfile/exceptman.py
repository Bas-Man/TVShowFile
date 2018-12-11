import os
import json


class ExceptionListManager:
    '''
        This class will load and save the exceptionList. this data will be
        stored in a directory named 'data' under the tvshowfile module
        directory

    '''

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
        self.file = "exceptionlist.json"

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
            rtype: ExceptionList of Dict
        '''

        with open(self.path + self.file, 'r') as fhandle:
            ExceptList = json.load(fhandle)

        return ExceptList
