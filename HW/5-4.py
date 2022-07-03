class Add1:
    
    def __init__(self, _sum):
        self._sum = _sum    
    
    def __call__(self, num):
        
        self._sum += num
        print(self._sum)
        return Add.__call__(self, num)
    
class Add(Add1):
    def __init__(self, _sum):
        self._sum = _sum
        
    def __str__(self):
        return f"{self._sum}"
    
    def __call__(self, num):
        self.num = super().__call__(num)
        return super().__call__(num)
    
print(Add(12)(4)(4))

#b = Add(12)(5)





    
