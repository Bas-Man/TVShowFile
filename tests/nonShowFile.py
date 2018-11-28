import unittest
from tvshowfile import TVShowFile


class TVShowFileTests(unittest.TestCase):

    def setUp(self):
        self.showFile = TVShowFile.TVShowFile("/tmp/file")

    def testFilePath(self):
        self.assertEqual(self.showFile.FilePath(), "/tmp/file")

    def testFilePathFalse(self):
        self.assertNotEqual(self.showFile.FilePath(), "/tmp/file2")

    def testAbsPath(self):
        self.assertEqual(self.showFile.absPath, "/tmp")

    def testFilename(self):
        self.assertEqual(self.showFile.filename, "file")

    def testFolderExists(self):
        self.assertTrue(self.showFile.folderExists())

    def testfileExists(self):
        self.assertTrue(self.showFile.fileExists())

class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = TVShowFile.TVShowFileParser("test.avi")

    def tearDown(self):
        self.filename = None

    def testObjVariblesNone(self):
        self.assertIsNone(self.filename.showName)
        self.assertIsNone(self.filename.season)
        self.assertIsNone(self.filename.episode)
        self.assertIsNone(self.filename.seasonEpisode)
        self.assertIsNone(self.filename.fileExt)
        
    def testgetShowData(self):
        self.assertTrue(self.filename.getShowData())
    
if __name__ == '__main__':
    unittest.main()
