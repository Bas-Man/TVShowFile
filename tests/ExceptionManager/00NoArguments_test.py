import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()

    def testObjVariblesDefaultandLoads(self):
        self.assertIsNotNone(self.handle)


if __name__ == '__main__':
    unittest.main()
