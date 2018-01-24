import pickle
import json

class CandlesImport():
    def __init__(self):
        pass
    
    def importFromPickle(self,filename):
        return pickle.load( open( filename, "rb" ) )

    def importFromJSON(self,filename):
        f = open(filename)
        return json.load(f)