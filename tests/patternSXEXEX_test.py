import unittest
from tvshowfile import TVShowFile


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = TVShowFile.TVShowFileParser("test.s01E01E02.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"test")
        self.assertEqual(self.filename.season, "01")
        self.assertIsNone(self.filename.episode)
        self.assertIsNone(self.filename.year)
        self.assertEqual(self.filename.firstEpisode,"01")
        self.assertEqual(self.filename.lastEpisode, "02")
        self.assertEqual(self.filename.seasonEpisode, "S01E01E02")
        self.assertEqual(self.filename.fileExt,"avi")
        
        print("\nName: " + self.filename.getShowName())
        print("Season: " + self.filename.getSeason())
        print("First Episode: " + self.filename.getFirstEpisode())
        print("Last Episode: " + self.filename.getLastEpisode())
        print("SeasonEpisode: " + self.filename.getSeasonEpisode())
        print("Ext: " + self.filename.getFileExt())
    
    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())
    
if __name__ == '__main__':
    unittest.main()
