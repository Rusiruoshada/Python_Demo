# A decorator is a function that takes another function and adds extra functionality to it.
# way to modify or extend the behavior of a function without changing its actual code
# basic structure for decorator :->
# def decorator(func):
    # def wrapper(*args, **kwargs):
    #     # extra code
    #     result = func(*args, **kwargs)
    #     # extra code
    #     return result
    # return wrapper

def greater_first_deco(func):
    def wrapper(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return wrapper

@greater_first_deco
def sub(a,b):
    return a-b
    
@greater_first_deco
def divide(a,b):
    return a/b

result1 = divide(10,20)
result2 = sub(2,4)

print('divide: ',result1," subtract: ",result2)


