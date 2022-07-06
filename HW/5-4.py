class Add(int):
    def __init__(self, num1):
        self.num1 = num1
        
    def __call__(self, num2):
        adds = self.num1 + num2
        return Add(adds)
    
print(Add(2)(5)(19))







    
