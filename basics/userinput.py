# to get user input we use input() method
# input return a string
input1 = int(input('enter a number: '))
input2 = int(input('enter second number: '))
# strip() use for trim -> start and end white spaces remove
input3 = input('what operand [+,*,/,-]: ').strip()

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def subtract(a,b):
    return a-b

# match case are equal to switch case
# case can have multiple search cases like case 300 | 200 | 400:
# switch case -> default option show as case _: -> wild card use '_'
# no break need in switch case
match(input3):
    case '+':
        print(add(input1,input2))        
    case '-':
        print(subtract(input1,input2))
    case '/':
        print(divide(input1,input2))
    case '*':
        print(multiply(input1,input2))
    case _:
        print('invalid input')