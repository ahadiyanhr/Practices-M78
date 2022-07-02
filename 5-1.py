class Sengleton():
    '''
    This class instantiated only one instance
    '''
    instance = 'FixedInstance'

    def __new__(cls):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls)
        return cls.instance
    

akbar = Sengleton()
asghar = Sengleton()
print(akbar == asghar)
print(id(akbar), id(asghar))