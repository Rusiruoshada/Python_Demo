# hight order function is a function that accept function as a argument
def square(num):
    return num *num

def cube(num):
    return num* num *num;

def operation(nums,callFunc):
    for n in nums:
        result = callFunc(n)
        print(n, ": ",result)

nums =[2,3,4,5,12]
operation(nums,cube)