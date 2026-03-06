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




