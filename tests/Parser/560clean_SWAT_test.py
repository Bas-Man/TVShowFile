import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("S.W.A.T.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename._showName, "S.W.A.T")
        self.assertEqual(self.filename._season, "01")
        self.assertEqual(self.filename._episode, "01")
        self.assertEqual(self.filename.seasonEpisode, "S01E01")
        self.assertEqual(self.filename._fileExt, "avi")
        self.assertIsNone(self.filename.firstEpisode)
        self.assertIsNone(self.filename.lastEpisode)
        self.assertIsNone(self.filename._year)
        self.assertEqual(self.filename.getShowNameOnly(), "S.W.A.T")
        self.assertTrue(self.filename.wasParsed)
        print("\nFile: " + self.filename.fileName)
        print("Name: " + self.filename.showName)
        print("ShowNameOnly: " + self.filename.getCleanShowName())
        print("Season: " + self.filename.season)
        print("Episode: " + self.filename.episode)
        print("SeasonEpisode: " + self.filename.seasonEpisode)
        print("Ext: " + self.filename.fileExt)
        if self.filename.wasParsed:
            print("wasParsed is True")

    def testgetCleanShowName(self):
        self.assertEqual(self.filename.getCleanShowName(), "S.W.A.T")


if __name__ == '__main__':
    unittest.main()
