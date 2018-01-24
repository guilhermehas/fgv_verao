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
            
    def get_candles(self,deltaDays):
        start = datetime.datetime.now()-datetime.timedelta(days=deltaDays)
        start_ts = int(start.timestamp())
        url = self.make_url(start_ts)
        candles_string = requests.get(url).content
        candles = simplejson.loads(candles_string)
        assert isinstance(candles,list)
        
        return candles