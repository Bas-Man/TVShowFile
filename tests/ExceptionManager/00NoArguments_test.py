import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()
        # Base data set
        self.handle.loadExceptionList()
        self.list = self.handle.exportList()
        self.expected = {}
        self.expected['s.w.a.t'] = {}
        self.expected['s.w.a.t']['name'] = 'S.W.A.T'
        self.expected['s.w.a.t']['keepPeriods'] = True
        self.expected['the.4400'] = {}
        self.expected['the.4400']['name'] = 'The 4400'
        self.expected['the.4400']['keepPeriods'] = False

    def testObjVariblesDefaultandLoads(self):
        self.assertDictEqual(self.list, self.expected)

    def testObjhasKey(self):
        self.assertTrue(self.handle.hasKey('s.w.a.t'))

    def testObjhasKeyisFalse(self):
        self.assertFalse(self.handle.hasKey('bogus'))

    def testObjkeepsPeriods(self):
        self.assertTrue(self.handle.keepsPeriods('s.w.a.t'))

    def testObjkeepsPeriodsFalse(self):
        self.assertFalse(self.handle.keepsPeriods('the.4400'))

    def testObjgetShowNameByKey(self):
        self.assertEqual(self.handle.getShowNameByKey('s.w.a.t'), "S.W.A.T")

if __name__ == '__main__':
    unittest.main()
