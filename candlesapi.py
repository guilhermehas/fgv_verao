import requests
import simplejson
import datetime

class candlesAPI():
    def __init__(self,pair, granularity = 300):
        self.pair = pair
        self.granularity = granularity

    def make_url(self,start):
        url = 'https://poloniex.com/public?command=returnChartData&currencyPair={}&{}'.format(self.pair,self.get_parameters_string(start))
        return url

    def get_parameters_string(self,start):
        parameters = [  'start={}'.format(start),
                        #'end={}'.format(end),
                        'period={}'.format(self.granularity)]
        
        join_string = '&'.join(parameters)
        return join_string

    def get_request(self,start):
        start_ts = int(start.timestamp())
        url = 'https://poloniex.com/public'
        parameters = {'command': 'returnChartData', 'currencyPair': self.pair,
                      'start': start_ts, 'period': self.granularity}
        return requests.get(url, params=parameters).content.decode('utf8')
            
    def get_candles(self,deltaDays):
        start = datetime.datetime.now()-datetime.timedelta(days=deltaDays)
        candles_string = self.get_request(start)
        candles = simplejson.loads(candles_string)
        assert isinstance(candles,list)
        
        return candles