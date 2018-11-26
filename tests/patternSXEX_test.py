import unittest
from tvshowfile import TVShowFile


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = TVShowFile.TVShowFileParser("test.s01E01.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"test")
        self.assertEqual(self.filename.season, "01")
        self.assertEqual(self.filename.episode,"01")
        self.assertIsNone(self.filename.seasonEpisode)
        self.assertEqual(self.filename.fileExt,"avi")
        
    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())
    
if __name__ == '__main__':
    unittest.main()
