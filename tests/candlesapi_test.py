from candlesapi import candlesAPI
import datetime
import unittest

class candlesAPI_test(unittest.TestCase):
    def test_get_parameters(self):
        btc_api = candlesAPI('USDT_BTC')
        parameters = btc_api.get_parameters_string(100)
        assert parameters == 'start=100&period=300'

    def test_make_url(self):
        btc_api = candlesAPI('USDT_BTC')
        url = btc_api.make_url(1514764800)
        assert url == 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1514764800&period=300'


    def test_get_candles(self):
        btc_api = candlesAPI('USDT_BTC')
        candles = btc_api.get_candles(20)
        assert len(candles) > 5

if __name__ == '__main__':
    unittest.main()
