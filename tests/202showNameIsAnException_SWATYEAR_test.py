import unittest
from context import parser

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("S.W.A.T.2017.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    # This should be false since we do not support year as part of ExceptionList
    def testisInExceptionList(self):
        self.assertFalse(self.filename.showNameIsAnException())

if __name__ == '__main__':
    unittest.main()
