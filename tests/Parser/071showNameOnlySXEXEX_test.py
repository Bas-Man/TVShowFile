import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.S01E01E02.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName, "test")
        self.filename.showNameOnly
        self.assertEqual(self.filename.showNameOnly, "test")
        self.assertEqual(self.filename._season, "01")
        self.assertIsNone(self.filename._episode)
        self.assertEqual(self.filename.firstEpisode, "01")
        self.assertEqual(self.filename.lastEpisode, "02")
        self.assertEqual(self.filename.seasonEpisode, "S01E01E02")
        self.assertEqual(self.filename._fileExt, "avi")

        print("\nName: " + self.filename.showName)
        print("Season: " + self.filename.season)
        print("First Episode: " + self.filename.getFirstEpisode())
        print("Last Episode: " + self.filename.getLastEpisode())
        print("SeasonEpisode: " + self.filename.seasonEpisode)
        print("Ext: " + self.filename.fileExt)
        print("Year: " + self.filename.year)
        print("ShowNameOnly: " + self.filename.showNameOnly)

    def testgetShowNameOnly(self):
        self.assertEqual(self.filename.showNameOnly, 'test')

    def testisMultiEpisode(self):
        self.assertTrue(self.filename.isMultiEpisode)


if __name__ == '__main__':
    unittest.main()
