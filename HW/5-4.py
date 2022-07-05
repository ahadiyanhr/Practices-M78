class NextCall:
    __num = 0
    
    def get_a(self):
        return self.__num
    def set_a(self, value):
        NextCall.__num = value
        
    def __call__(self):
        return self.__call__(NextCall.__num)

    
class Add(NextCall):
    def __init__(self, num1):
        self.num1 = num1
        NextCall.__num = num1
        
    def __call__(self, num2):
        NextCall.__num += num2
        print(NextCall.__num)
        NextCall.__call__(self)
        
    
print(Add(2)(4)(10))







    
