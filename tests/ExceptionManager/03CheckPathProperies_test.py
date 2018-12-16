import unittest
import os
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()

    def testDefaultPath(self):
        self.assertEqual(self.handle.path, os.path.dirname(
            os.getcwd() + "/tvshowfile/data/") + "/")

    def testNewPathSet(self):
        self.handle.path = "/tmp/"
        self.assertEqual(self.handle.path, "/tmp/")

    def testInvalidatePath(self):

        self.handle.path = "/tm"
        self.assertEqual(self.handle.path,
                         os.path.dirname(os.getcwd()
                                         + "/tvshowfile/data/") + "/")

    def testValidPathInvalidPermissions(self):

        self.handle.path = "/etc/"
        self.assertEqual(self.handle.path,
                         os.path.dirname(os.getcwd()
                                         + "/tvshowfile/data/") + "/")


if __name__ == '__main__':
    unittest.main()
