import unittest
from context import parser

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("S.W.A.T.s01E01.1080p.avi")

    def testgetCleanShowName(self):
        self.assertEqual(self.filename.getCleanShowName(), "S.W.A.T")

if __name__ == '__main__':
    unittest.main()
