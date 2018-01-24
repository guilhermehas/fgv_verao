import unittest
from candlesimport import *


class candlesImport_test(unittest.TestCase):

    def test_importFromPickle(self):
        ci = CandlesImport()
        candles = ci.importFromPickle('candles30.p')
        self.verifyCandles(candles)

    def test_importFromJson(self):
        ci = CandlesImport()
        candles = ci.importFromJSON('candles30.json')
        self.verifyCandles(candles)
    
    def verifyCandles(self,candles):
        assert isinstance(candles,list)
        assert len(candles) > 5


if __name__ == '__main__':
    unittest.main()