import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.s01E01E02.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"test")
        self.assertEqual(self.filename.season, "01")
        self.assertIsNone(self.filename.episode)
        self.assertIsNone(self.filename.year)
        self.assertEqual(self.filename.firstEpisode,"01")
        self.assertEqual(self.filename.lastEpisode, "02")
        self.assertEqual(self.filename.seasonepisode, "S01E01E02")
        self.assertEqual(self.filename._fileExt,"avi")

        print("\nName: " + self.filename.getShowName())
        print("Season: " + self.filename.season)
        print("First Episode: " + self.filename.getFirstEpisode())
        print("Last Episode: " + self.filename.getLastEpisode())
        print("SeasonEpisode: " + self.filename.seasonepisode)
        print("Ext: " + self.filename.fileext)

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

if __name__ == '__main__':
    unittest.main()
