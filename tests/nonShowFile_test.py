import unittest
from tvshowfile import TVShowFile

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = TVShowFile.TVShowFileParser("test.avi")

    def tearDown(self):
        self.filename = None

    def testObjVariblesNone(self):
        self.assertIsNone(self.filename.showName)
        self.assertIsNone(self.filename.season)
        self.assertIsNone(self.filename.episode)
        self.assertIsNone(self.filename.seasonEpisode)
        self.assertIsNone(self.filename.fileExt)
        self.assertIsNone(self.filename.quality)

    def testgetShowData(self):
        self.assertFalse(self.filename.getShowData())
    
if __name__ == '__main__':
    unittest.main()
