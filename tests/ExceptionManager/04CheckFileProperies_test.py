import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()

    def testDefaultFile(self):
        self.assertEqual(self.handle.file, "exceptionlist.json")

    def testNewFileSet(self):
        self.handle.file = "test.json"
        self.assertEqual(self.handle.file, "test.json")


if __name__ == '__main__':
    unittest.main()
