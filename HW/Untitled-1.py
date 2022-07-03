class Bar(object):
    def __init__(self):
        self.value = ''
    def __get__(self, instance, owner):
        print("instance: ",instance == f)
        print("owner: ",owner == Foo)
        return self.value
    def __set__(self, instance, value):
        print("instance: ",instance == f)
        print("value: ",value == 10)
        self.value = value

class Foo(object):
    bar = Bar()

f = Foo()
f.bar = 10
print(f.bar)