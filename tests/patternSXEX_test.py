import unittest
from tvshowfile import TVShowFile


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = TVShowFile.TVShowFileParser("test.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"test")
        self.assertEqual(self.filename.season, "01")
        self.assertEqual(self.filename.episode,"01")
        self.assertEqual(self.filename.seasonEpisode, "S01E01")
        self.assertEqual(self.filename.fileExt,"avi")
        self.assertIsNone(self.filename.firstEpisode)
        self.assertIsNone(self.filename.lastEpisode)
        self.assertIsNone(self.filename.year)
        self.assertEqual(self.filename.quality,"1080p")
        print("\nName: " + self.filename.getShowName())
        print("Season: " + self.filename.getSeason())
        print("Episode: " + self.filename.getEpisode())
        print("SeasonEpisode: " + self.filename.getSeasonEpisode())
        print("Quality: " + self.filename.getQuality())
        print("Ext: " + self.filename.getFileExt())

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testhasYear(self):
        self.assertFalse(self.filename.year, "Year is False as filename does not contain a Year")

    def testisMultiEpisode(self):
        self.assertFalse(self.filename.multiEpisode)
    
if __name__ == '__main__':
    unittest.main()