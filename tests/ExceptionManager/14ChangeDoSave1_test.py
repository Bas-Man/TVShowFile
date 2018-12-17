import unittest
from context import exceptman


class ExceptmanTests(unittest.TestCase):

    def setUp(self):
        self.handle = exceptman.ExceptionListManager()
        self.list = self.handle.loadExceptionList()
        self.handle._updated = True

        self.expected = {}
        self.expected['s.w.a.t'] = {}
        self.expected['s.w.a.t']['name'] = 'S.W.A.T'
        self.expected['s.w.a.t']['keepPeriods'] = True
        self.expected['the.4400'] = {}
        self.expected['the.4400']['name'] = 'The 4400'
        self.expected['the.4400']['keepPeriods'] = False
        self.expected['doctor who'] = {}
        self.expected['doctor who']['name'] = 'Doctor Who'

    def testExceptListNotSaved(self):
        self.assertTrue(self.handle.saveExceptionList(self.expected))


if __name__ == '__main__':
    unittest.main()
