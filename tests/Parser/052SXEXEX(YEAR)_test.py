import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.(2018).s01E01E02.avi")

    def tearDown(self):
        self.filename = None

    def testObjValuesSet(self):
        self.assertEqual(self.filename.showName,"test.(2018)")
        self.assertEqual(self.filename.season, "01")
        self.assertIsNone(self.filename.episode)
        self.assertEqual(self.filename.year,'2018')
        self.assertEqual(self.filename.firstEpisode,"01")
        self.assertEqual(self.filename.lastEpisode, "02")
        self.assertEqual(self.filename.seasonepisode, "S01E01E02")
        self.assertEqual(self.filename.fileExt,"avi")

        print("\nName: " + self.filename.getShowName())
        print("Season: " + self.filename.season)
        print("First Episode: " + self.filename.getFirstEpisode())
        print("Last Episode: " + self.filename.getLastEpisode())
        print("SeasonEpisode: " + self.filename.seasonepisode)
        print("Ext: " + self.filename.getFileExt())

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testisMultiEpisode(self):
        self.assertTrue(self.filename.multiEpisode)

    def testhasYear(self):
        self.assertTrue(self.filename.year,
            "Year is True as filename does not contain a Year")

if __name__ == '__main__':
    unittest.main()
