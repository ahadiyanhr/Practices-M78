class Number(int,float):
    
    def __new__(cls, number):
        self = object.__new__(number)
        self.__init__(number)
        
        if isinstance(number,int):
            return int(number)
        elif isinstance(number,float):
            return float(number)
        
    def __init__(self, number):
        self._number = number
        
            