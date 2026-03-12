class computer:
    brand = 'ROMs' # class variable(it like static variable in java)
    # __init__ is a method that run automatically when you create an object from a class. like java  constructor method but not the constructor. this how we set instances variable
    def __init__(self,cpu,ram): # here self is compulsory, and to pass values we separately set them
        self.cpu = cpu # local variable(instance variable)
        self.ram = ram

    def config(self): # there are no compulsory to use self(in java we call this)
        print('config: ',self.cpu, self.ram)

c = computer('i7','DDR4 8GB') # type of the instance
d = computer('i3','DDR3 4GB')
print(type(computer)) # <class 'type'>
# it show class as type In Python, classes themselves are objects. And the type of a class object is type.
print(type(c)) # <__main__.computer>

# self like when we want to use method in side a class we have to give what obj refer, so we pass the obj that we work
computer.config(c)
c.config() # we can do that same here but don't have to specify the class. here when we getting c as the obj of computer so we can access the config(). c obj automatically pass so self get c as the obj
d.config()

