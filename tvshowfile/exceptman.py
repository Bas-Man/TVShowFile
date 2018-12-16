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

        if path is None:
            self._path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
        else:
            self._path = path

        if file is None:
            self._file = "exceptionlist.json"
        else:
            self._file = file

        self.__ValidatePathFile()

    def __ValidatePathFile(self):
        '''
            Check that the directory structure and file are valid for loading
            If either are not valid raise and OSError
        '''
        if not os.path.exists(self._path):
            raise OSError(
                errno.ENOENT, os.strerror(errno.ENOENT), self._path
            )

        if not os.path.isfile(self._path + self._file):
            raise OSError(
                errno.ENOENT, os.strerror(errno.ENOENT), self._file)

    @property
    def path(self):
        '''
            Return the path to data directory.
            rtype: Str
        '''
        return self._path

    @path.setter
    def path(self, path):
        '''
            Set the path if it not the default. If the path is not valid or
            the user does not have write access the default location is used

        '''
        if os.path.exists(path):
            if os.access(path, os.W_OK):
                self._path = path
            else:
                print("You do not have write permissions to this location.")
        else:
            print("This is not a valid directory path.")

    @property
    def file(self):
        '''
            Return the name of the data file.
            rtype: Str
        '''
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    def loadExceptionList(self):
        '''
            Load the json ExceptionList data from the json file.
            rtype: ExceptionList, which is a nested Dictionary
            returns None if loading of file fails
        '''

        try:
            with open(self._path + self._file, 'r') as fhandle:
                ExceptList = json.load(fhandle)
        except OSError:
            print("Unable to open file.")
            return None

        return ExceptList

    def saveExceptionList(self):
        '''
            This will save the nested dictionary that is the ExceptionList
            This should be called when if the contents of the dictionary has
            been changed
            rtype: Success or Failure value?
            # TODO: NotImplemented
            # IDEA: If FileNotFoundError Change directory to /tmp
        '''
        pass
