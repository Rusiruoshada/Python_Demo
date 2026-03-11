# to create function we use def keyword
# in python we don't use {} to show scope of a function we use indentation(tab or space)
def add(a,b) :
    return a*b

print(add(10,12))

# variable length arguments in def
def add(a:int,*b:int): # when passing arg to def we can strictly specify how many we allows, but using *varName its help to do any number of parameters to def it covert it to a tuple 
    sum = a 
    for n in b:
        sum += n
    return sum

print(add(12,30,23,43,12))

# keyword arguments in def
# when we don't know how the argument order(like (name,age)) we have to check if we want to give right parameter to right argument.
# in keyword argument we specify the what argument we given the value so order doesn't matter
def divide(num1,num2):
    return num1 - num2

print(divide(num1=12,num2=32))

# keyword variable length arguments
# combine of keyword and variable length argument type way
# use ** to represent dict type, * for tuple
def info(name,**keyArgs):
    print('username: ',name,end=' | ')
    for key,value in keyArgs.items():
        print(key,': ', value, end=' | ')
    print()
info(name='roms',age=12,address='Sri lanka',tech='python')

# anonymous function (lambda)
# to use it we have to use lambda keyword
fun = lambda num1,num2 : num1 * num2
print(fun(5,4))


