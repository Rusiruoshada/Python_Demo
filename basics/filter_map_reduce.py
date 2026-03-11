# filter
nums:int = [4,5,2,6,8,12,32,13,19,10]

# filter func in python take 2 parameters: function and iterative variable
# function will be the way to say how to filter 
# and iterative variable, filter function will send one by one to our function, only condition true will return
result = list(filter(lambda n : n%2==0,nums)) # result will show as a obj so we use list()/tuple()/set() func to get the data
print(result)

# map
# map also work as filter() 
# only different is filter show our logic true values, map will do the calculation and return the result one by one
result1 = list(map(lambda n:n*2,result))
print(result1)

# reduce
# reduce is a function that we can use to get one output base one our logic
# first we have to import it from functools
from functools import reduce
sum = reduce(lambda n1,n2: n1+n2,result1)
print(sum)


