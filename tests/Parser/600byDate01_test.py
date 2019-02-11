import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("Jimmy.Fallon.2019.01.29.Matthew.Broderick.720p.HDTV.x264-SORNY[eztv].mkv")

    def tearDown(self):
        self.filename = None

    def testWasParsed(self):
        self.assertTrue(self.filename.wasParsed)

    def testObjValuesSet(self):
        self.assertEqual(self.filename._showName, "Jimmy.Fallon")
        self.assertEqual(self.filename._fileExt, "mkv")
        self.assertEqual(self.filename.getShowNameOnly(), "Jimmy.Fallon")
        self.assertTrue(self.filename.wasParsed)
        print("\nFile: " + self.filename.fileName)
        print("Name: " + self.filename.showName)
        print("Year: " + self.filename.year)
        print("Month: " + self.filename.month)
        print("Date: " + self.filename.date)
        # print("ShowNameOnly: " + self.filename.getCleanShowName())
        print("Ext: " + self.filename.fileExt)
        if self.filename.wasParsed:
            print("wasParsed is True")

    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())

    def testgetCleanShowName(self):
        self.assertTrue(self.filename.getCleanShowName(), "jimmy fallon")


if __name__ == '__main__':
    unittest.main()
