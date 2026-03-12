class A:
    def f1(self):
        print('f1 work')
    
    def f2(self):
        print('f2 work')
    
    def show(self):
        print('show A')

# this is single level inheritance
class B(A):# this is the way to say B get all from A(B inherit A) 
    def f3(self):
        print('f3 work')
    
    def f4(self):
        print('f4 work')
    def show(self):
        print('show B')

class C(B):# C inherit from B so this is multi level inheritance
    def f5(self):
        print('f5 work') 
    def show(self):
        print('show C')

class D(A,B): # this is multiple inheritance
    def show(self): # when we call show first look for that in own if not there then from parent
        print('show D')


obj1 = A()
obj1.f1()
obj2 = D()
obj2.show() #if the class D don't have the method then first check A then B. it happen because the order we give in class D(A,B)  this technique is Method resolution Order(MRO)


