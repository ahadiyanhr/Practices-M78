import pickle

class Pickling:
    def __init__(self, name: str):
        self.name = name
 
    def push(self, data):
        with open(self.name, 'ab') as f:
            return pickle.dump(data, f)
    
    def pull(self):
        with open(self.name, 'rb') as f:
            return pickle.load(f)
        
