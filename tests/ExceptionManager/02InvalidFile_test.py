import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()
        self.handle.path = "/tm"

    def testValidatePathFile(self):

        with self.assertRaises(OSError) as cm:
            self.handle = exceptman.ExceptionListManager(file="bogus")

        err = cm.exception
        self.assertEqual(str(err),
                         "[Errno 2] No such file or directory: 'bogus'")


if __name__ == '__main__':
    unittest.main()
