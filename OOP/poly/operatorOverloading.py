class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance = balance

    def __str__(self): # method overriding
        return f'{self.name} : {self.balance}' # use f for use particular format
    
    def __add__(me,you): # no need to self but we use self. its common knowledge
        return Account('combined', me.balance + you.balance) 
    
    def __gt__(self,other):
        return self.balance > other.balance

user1 = Account('rm',1000)
user2 = Account('dm',2000)

# every thing in python is a object
# when we try to print user1 obj we don't get the values instead we get __main__.className and memory address 
# but when we print a its show the value right?
# it happen because when we call print(a) its automatically run like a.__str__() this why we get the value
# so every obj have __str__() to return value
a = 10
b = 20
print(user1)
print(a.__str__())
print(user1.__str__()) # if __str__() not define -> <__main__.Account object at 0x7e2009934800>

# to get the value in obj we have to override the __self__() in obj 
# __str__() is a class type method
print(user1.__str__())
print(user2)

# we can easily add to numbers and print
c = a+b
print(c) # 30
# but what about class obj we create
# we can't add it normally, for do that we have to use __add__() 
print(a.__add__(b)) # 30
print(int.__add__(a,b)) # 30

# combine = user1 + user2 -> normally we can't do this
# to do that we have to method overload and change __add__()
combine = user1 + user2
print(combine)

# normally we can't compare class objs
# to do it there are method like __str__() or __add__() 
# __gt__() -> greater than , __ge__() -> greater than or equal , __ne__() -> not equal
if(user1.__gt__(user2)):
    print('user1 is greater than user2')
else:
    print('user2 is greater than user1')


