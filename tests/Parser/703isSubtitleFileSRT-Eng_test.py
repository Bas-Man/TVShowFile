import unittest
from context import parser


class TVShowFileParserTests(unittest.TestCase):

    def setUp(self):
        self.filename = parser.Parser("test.2018.S01E01E02.Eng.srt")

    def tearDown(self):
        self.filename = None

    def testSubtitleIsEng(self):
        self.assertEqual(self.filename.subLanguage, 'Eng')


if __name__ == '__main__':
    unittest.main()
