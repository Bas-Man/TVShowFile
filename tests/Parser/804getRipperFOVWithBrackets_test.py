import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.2018.S01E01E02.[fov].avi")

    def tearDown(self):
        self.filename = None

    def testRipperFOVWithBrackets(self):
        self.assertEqual(self.filename.ripper, "fov")


if __name__ == '__main__':
    unittest.main()
