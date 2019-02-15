import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.2018.s01E01.1080p.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName, "test.2018")
        self.assertEqual(self.filename._season, "01")
        self.assertEqual(self.filename._episode, "01")
        self.assertEqual(self.filename._seasonEpisode, "S01E01")
        self.assertEqual(self.filename._fileExt, "avi")
        self.assertIsNone(self.filename.firstEpisode)
        self.assertIsNone(self.filename.lastEpisode)
        self.assertEqual(self.filename.year, '2018')
        self.assertEqual(self.filename._resolution, "1080p")
        self.assertTrue(self.filename.wasParsed)
        print("\nFile: " + self.filename.fileName)
        print("Name: " + self.filename.showName)
        print("Season: " + self.filename.season)
        print("Episode: " + self.filename.episode)
        print("SeasonEpisode: " + self.filename.seasonEpisode)
        print("Resolution: " + self.filename.resolution)
        print("Ext: " + self.filename.fileExt)
        if self.filename.wasParsed:
            print("wasParsed is True")

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testhasYear(self):
        self.assertTrue(self.filename.year,
                        "Year is True as filename does not contain a Year")

    def testisMultiEpisode(self):
        self.assertFalse(self.filename.isMultiEpisode)


if __name__ == '__main__':
    unittest.main()
