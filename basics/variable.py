# python variable we don't have to set datatype
a = 10
b = 10
c = 11

# getting memory address
print(id(a)) # 11755976
print(id(b)) # 11755976
print(id(c)) # 11756008
# in python if variable have same value then both variable assign same memory address
# when we change the value of that same address variable
# its create another memory address that not same as previous one
# if there no variable assign values will delete by python garbage collector
# all these work for numbers or strings in compile time, if we use runtime its can be different

a = 256+1
b = int("257")
c = "".join(['hello welcome to',' o kawai koto that even worst right its beyond pathetic'])
d = 'hello welcome to o kawai koto that even worst right its beyond pathetic'

print(a is b) 
print(c is d)

# in python we can print true or false convert to int() -> 1 and 0
# and python is case sensitive
print(int(True)) # 1
print(int(False)) # 0

# datatype -> range
r = range(10) # start from 0 and to given number BY default
print(r) # range(0,10)
print(type(r)) # class 'range'
print(set(r)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set(range(2,11,1))) # this will start from 2 and end 10, we can specify how next number get too.
print(set(range(2,11,2))) # {2, 4, 6, 8, 10}

# assign multiple at once
a,b,c = 5,3, 'hello'
print(a);
print(b);
print(c);

# LOGICAL operators
# and, or , not -> logical operators
# & , | , ~, ^, <<,>>  -> bitwise
print(a>2 | b<2) 
print(type(a>2 | b<2))

# variable swapping in python
# this happen concept call tuple packing and unpacking
# right side tuple packing(b,a -> (b,a)) then when we assign to left its unpack(a,b = [b,a])
a,b = 6,5
a,b = b,a
print(a)
print(b)

# print all the global variables
globalVar = globals() # its show a obj that contain all the global variables even user define functions
print(globalVar) # output: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7390a21fcd40>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/local2/Edu/Projects/DevOps/python/Python_Demo/basics/variable.py', '__cached__': None, 'a': 5, 'b': 6, 'c': 'hello', 'd': 'hello welcome to o kawai koto that even worst right its beyond pathetic', 'r': range(0, 10), 'globalVar': {...}}

#__name__ global variable
# default value for __name__ is __main__
# when we import a file its __name__ be file name not __main__ 
# only show __main__ when we run it in same file
# so this is useful when we want to run particular code in original file but not when we import it in other modules(files) 
# so we can check using if __name__ == '__main__' that mean its the same file
print(__name__)
