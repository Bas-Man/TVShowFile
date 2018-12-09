import unittest
from context import parser

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("the.4400.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"the.4400")
        self.assertEqual(self.filename.season, "01")
        self.assertEqual(self.filename.episode,"01")
        self.assertEqual(self.filename.seasonEpisode, "S01E01")
        self.assertEqual(self.filename.fileExt,"avi")
        self.assertIsNone(self.filename.firstEpisode)
        self.assertIsNone(self.filename.lastEpisode)
        self.assertIsNone(self.filename.year)
        self.assertEqual(self.filename.getShowNameOnly(),"the.4400")
        self.assertTrue(self.filename.wasParsed)
        print("\nFile: " + self.filename.getFilename())
        print("Name: " + self.filename.getShowName())
        print("ShowNameOnly: " + self.filename.getCleanShowName())
        print("Season: " + self.filename.getSeason())
        print("Episode: " + self.filename.getEpisode())
        print("SeasonEpisode: " + self.filename.getSeasonEpisode())
        print("Ext: " + self.filename.getFileExt())
        if self.filename.wasParsed():
            print("wasParsed is True")


    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testgetCleanShowName(self):
        self.assertTrue(self.filename.getCleanShowName(),"the 4400")

if __name__ == '__main__':
    unittest.main()
