class employee:

    def __new__(cls): # this the python constructor
        print('calling the constructor')
        # we have to manually call the init 
        return super(employee,cls).__new__(cls)

        

    def walk(self):
        print(' is running')
    
    def __init__(self):
        print('init called')


obj1 = employee()
obj1.walk()
obj2 = employee.__new__(employee) # use to create a obj by specify class, use argument -> class
obj2.walk() # in here init not get call because we manually set constructor above line.









