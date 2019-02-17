import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.2018.S01E01E02.ettv.avi")

    def tearDown(self):
        self.filename = None

    def testRipperETTVNoBrackets(self):
        self.assertEqual(self.filename.ripper, "ettv")


if __name__ == '__main__':
    unittest.main()
