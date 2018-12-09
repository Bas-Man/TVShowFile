import unittest
from context import parser

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.avi")

    def tearDown(self):
        self.filename = None

    def testObjVariblesNone(self):
        self.assertIsNone(self.filename.showName)
        self.assertIsNone(self.filename.season)
        self.assertIsNone(self.filename.episode)
        self.assertIsNone(self.filename.seasonEpisode)
        self.assertIsNone(self.filename.fileExt)
        self.assertIsNone(self.filename.resolution)


    def testgetShowData(self):
        self.assertFalse(self.filename.getShowData())

    def testFileNotValid(self):
        self.assertFalse(self.filename.Parsed)

if __name__ == '__main__':
    unittest.main()
