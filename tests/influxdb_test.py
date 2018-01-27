from influxdb import *
import unittest

class candlesImport_test(unittest.TestCase):
    def test_writepoints(self):
        infDB = influxdb('localhost',8086,'root','root','poloniex')
        req = infDB.write_points('xxx',self.getPoints())
        assert req.status_code == 200

    def getPoints(self):
        return [\
    {\
        "date": 1514764800,\
        "high": 13799.99999984,\
        "low": 13710.00000001,\
        "open": 13799.99999984,\
        "close": 13720.00000005,\
        "volume": 158581.24115918,\
        "quoteVolume": 11.52611366,\
        "weightedAverage": 13758.43114488\
    },\
    {\
        "date": 1514765100,\
        "high": 13733.22823089,\
        "low": 13603,\
        "open": 13720.00000005,\
        "close": 13625.14125469,\
        "volume": 379166.9307217,\
        "quoteVolume": 27.75445766,\
        "weightedAverage": 13661.47864846\
    }]

if __name__ == '__main__':
    unittest.main()