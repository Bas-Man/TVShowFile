import unittest
from context import parser

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("the.4400.s01E01.1080p.avi")

    def testgetCleanShowName(self):
        self.assertEqual(self.filename.getCleanShowName(), "The 4400")

if __name__ == '__main__':
    unittest.main()
