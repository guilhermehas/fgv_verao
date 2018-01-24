from candlesapi import candlesAPI
import datetime

def test_get_parameters():
    btc_api = candlesAPI('BTC-USD')
    parameters = btc_api.get_parameters_string(100)
    assert parameters == 'start=100&granularity=300'

def test_make_url():
    btc_api = candlesAPI('BTC-USD')
    url = btc_api.make_url(200)
    assert url == 'https://api.gdax.com/products/BTC-USD/candles?start=200&granularity=300'


def test_get_candles():
    btc_api = candlesAPI('BTC-USD')
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=20)
    candles = btc_api.get_candles(start)
    assert len(candles) > 5
    #assert False

#test_get_candles()