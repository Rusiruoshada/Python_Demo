a = input('Enter number1: ')
b = input('Enter number2: ')

try: # try block have to use with either one except or finally blocks
    c = int(a)/int(b)
    print("result is ",c)
except ZeroDivisionError as zde:
    print('error occurred: ',zde)
except ValueError as ve:
    print('error occurred: ',ve)
except Exception as e:
    print('error occurred: ', e)
finally: # this run either find exception or not
    print('db connection is closed')

print('end of execution!')







