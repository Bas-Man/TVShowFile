import unittest
from context import tvshowfile


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = tvshowfile.tvshowfile.TVShowFileParser("test.2018.S01E01E02.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"test.2018")
        self.assertEqual(self.filename.season, "01")
        self.assertIsNone(self.filename.episode)
        self.assertEqual(self.filename.firstEpisode,"01")
        self.assertEqual(self.filename.lastEpisode, "02")
        self.assertEqual(self.filename.seasonEpisode, "S01E01E02")
        self.assertEqual(self.filename.fileExt,"avi")
        self.assertEqual(self.filename.year, "2018")
        
        print("\nName: " + self.filename.getShowName())
        print("Season: " + self.filename.getSeason())
        print("First Episode: " + self.filename.getFirstEpisode())
        print("Last Episode: " + self.filename.getLastEpisode())
        print("SeasonEpisode: " + self.filename.getSeasonEpisode())
        print("Ext: " + self.filename.getFileExt())
        print("Year: " + self.filename.getYear())

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testhasYear(self):
        self.assertTrue(self.filename.hasYear())

    def testisMultiEpisode(self):
        self.assertTrue(self.filename.isMultiEpisode())
    
if __name__ == '__main__':
    unittest.main()
