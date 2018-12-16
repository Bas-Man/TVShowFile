import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()
        # Base data set
        self.list = self.handle.loadExceptionList()
        self.expected = {}
        self.expected['s.w.a.t'] = {}
        self.expected['s.w.a.t']['name'] = 'S.W.A.T'
        self.expected['s.w.a.t']['keepPeriods'] = True
        self.expected['the.4400'] = {}
        self.expected['the.4400']['name'] = 'The 4400'
        self.expected['the.4400']['keepPeriods'] = False

    def testObjVariblesDefaultandLoads(self):
        self.assertDictEqual(self.list, self.expected)


if __name__ == '__main__':
    unittest.main()
