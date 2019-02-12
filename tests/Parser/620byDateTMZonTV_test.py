import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("TMZ.on.TV.2019.01.28.480p.x264-mSD[eztv].mkv")

    def tearDown(self):
        self.filename = None

    def testWasParsed(self):
        self.assertTrue(self.filename.wasParsed)

    def testObjValuesSet(self):
        self.assertEqual(self.filename._showName, "TMZ.on.TV")
        self.assertEqual(self.filename._fileExt, "mkv")
        self.assertEqual(self.filename.getShowNameOnly(), "TMZ.on.TV")
        self.assertTrue(self.filename.wasParsed)
        print("\nFile: " + self.filename.fileName)
        print("Name: " + self.filename.showName)
        print("Year: " + self.filename.year)
        print("Month: " + self.filename.month)
        print("Date: " + self.filename.date)
        print("ShowNameOnly: " + self.filename.getCleanShowName())
        print("Ext: " + self.filename.fileExt)
        if self.filename.wasParsed:
            print("wasParsed is True")

    def testgetCleanShowName(self):
        self.assertEqual(self.filename.getCleanShowName(), "TMZ on TV")


if __name__ == '__main__':
    unittest.main()
