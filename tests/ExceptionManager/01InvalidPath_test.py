import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def testValidatePathFile(self):

        with self.assertRaises(OSError) as cm:
            self.handle = exceptman.ExceptionListManager(path="/tm")

        err = cm.exception
        self.assertEqual(str(err),
                         "[Errno 2] No such file or directory: '/tm'")


if __name__ == '__main__':
    unittest.main()
