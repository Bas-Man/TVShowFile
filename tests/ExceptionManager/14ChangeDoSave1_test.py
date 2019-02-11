import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()
        self.handle.loadExceptionList()
        self.handle._updated = True

        self.handle.ExceptList['doctor who'] = {}
        self.handle.ExceptList['doctor who']['name'] = 'Doctor Who'

    def testExceptListNotSaved(self):
        self.assertTrue(self.handle.saveExceptionList())


if __name__ == '__main__':
    unittest.main()
