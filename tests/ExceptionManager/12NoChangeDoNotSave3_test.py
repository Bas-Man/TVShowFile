import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()

    def testExceptListNotSaved(self):
        self.assertFalse(self.handle.saveExceptionList(), "No List provided.")
        self.assertFalse(self.handle.updated)


if __name__ == '__main__':
    unittest.main()
