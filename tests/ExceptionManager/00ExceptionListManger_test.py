import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()

    def testObjVariblesNone(self):
        print(self.handle.getPath())
        print(self.handle.loadExceptionList())


if __name__ == '__main__':
    unittest.main()
