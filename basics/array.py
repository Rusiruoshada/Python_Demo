# array used to store same datatype
# in python to specify what the type of the array we have to specify a char first

# we can use just import package -> import everything
# or use from <package> import methods we want
from array import *

arr = array('i',[21,32,12,43,23,54])
# in here i mean int sign(positive values)
# there are sign(positive) and unsign(negative) its can show by i or I

print(arr.tolist()) #[21, 32, 12, 43, 23, 54]

print(arr.buffer_info()) # (125430338592656, 6) -> memory address and array size

arr.append(90) # add to end

arr1 = arr
print(arr1 is arr) # true, when we copy like this both arrays refer to same memory address so when changing one its change both -> because its refer to same memory address

# to only copy a array not use reference 
arr2 = array(arr.typecode,arr.tolist()) #typecode show the array type -> ('i')
arr3 = array(arr.typecode,(n for n in arr)) # this a another way to do it using for loop to loop through the array
print(arr is arr2) # false
print(arr is arr3) # false


