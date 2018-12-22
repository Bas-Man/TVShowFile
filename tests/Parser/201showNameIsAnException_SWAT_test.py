import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("S.W.A.T.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testisInExceptionList(self):
        self.assertTrue(self.filename.showNameIsAnException())


if __name__ == '__main__':
    unittest.main()
