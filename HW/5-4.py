class Add1:
    # def __init__(self, num1):
    #     print("In 0")
    #     self.num1 = num1    
    def __call__(self, num):
        print("In 1")
        self.sum = self.sum + num
        Add(self.sum).__call__(num)
    
class Add(Add1):
    def __init__(self, sum):
        print("In 2")
        self.sum = sum
    
    def __add__(self,sum):
        return self+sum
        
    def __call__(self, sum):
        print("In 4")
        print(self.sum)
        super().__call__(sum)
        
    
print(Add(2)(4)(10))







    
