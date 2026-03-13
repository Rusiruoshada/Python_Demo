class A:
    def show(self):
        print('in A')

class B(A):
    def show(self):
        print('in B')

obj1 = B()
obj1.show() # this will trigger the show in B class obj1 but if B class doesn't have the show method then its call the A class show method

# basically we override the show in A class 
