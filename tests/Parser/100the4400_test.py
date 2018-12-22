import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("the.4400.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename._showName, "the.4400")
        self.assertEqual(self.filename._season, "01")
        self.assertEqual(self.filename._episode, "01")
        self.assertEqual(self.filename.seasonEpisode, "S01E01")
        self.assertEqual(self.filename._fileExt, "avi")
        self.assertIsNone(self.filename.firstEpisode)
        self.assertIsNone(self.filename.lastEpisode)
        self.assertIsNone(self.filename._year)
        self.assertEqual(self.filename.getShowNameOnly(), "the.4400")
        self.assertTrue(self.filename.wasParsed)
        print("\nFile: " + self.filename.fileName)
        print("Name: " + self.filename.showName)
        print("ShowNameOnly: " + self.filename.getShowNameOnly())
        print("Season: " + self.filename.season)
        print("Episode: " + self.filename.episode)
        print("SeasonEpisode: " + self.filename.seasonEpisode)
        print("Ext: " + self.filename.fileExt)
        if self.filename.wasParsed:
            print("wasParsed is True")


    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testhasYear(self):
        self.assertFalse(self.filename.year,
            "Year is False as filename does not contain a Year")

    def testisMultiEpisode(self):
        self.assertFalse(self.filename.multiEpisode)

if __name__ == '__main__':
    unittest.main()
