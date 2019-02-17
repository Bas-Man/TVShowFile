import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.2018.S01E01E02.ssa")

    def tearDown(self):
        self.filename = None

    def testisSubtitleFileSSA(self):
        self.assertTrue(self.filename.isSubs)


if __name__ == '__main__':
    unittest.main()
