import unittest
from context import importer


class TVShowFileTests(unittest.TestCase):

    def setUp(self):
        self.showFile = importer.TVShowFile("/tmp/file")

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
