class Abc:
    b = 'class variable'
    def __init__(self,c=0,d=0):
        self.c = c # instance variable
        self.d = d

    # if we want to get class variable we can use direct way or create a method that return it
    @classmethod # this will say this method belong to class, not the objs
    def info(cls):
        return cls.b
    
    @staticmethod # in python static method used to show this method not work as class or instance types
    def gb_to_byte(gb):
        return gb * (1024 ** 3)


obj1 = Abc()
print(obj1.info()) # or can use class name Abc.info()
print(obj1.gb_to_byte(16))
