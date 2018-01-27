import requests
import json

class influxdb():
    def __init__(self,ip,port,user,password,db):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.db = db
    
    def write_points(self,name,points_dict):
        url = 'http://{}:{}/db/{}/series'.format(self.ip, self.port, self.db)
        params = {'u': self.user, 'p': self.password, 'time_precision': 's'}
        
        columns = list(points_dict[0].keys())
        def pointDict_to_list(point):
            return [*map(point.get,columns)]
        points = [*map(pointDict_to_list,points_dict)]

        data = [{'name': name, 'columns': columns, 'points': points}]
        return requests.post(url,data=json.dumps(data), params=params)
   
    
    def query(self,query):
        pass