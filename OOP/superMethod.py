class A:
    def __init__(self):
        print('in A init')

    def f1(self):
        print('f1 works')

class B(A):
    def __init__(self):
        super().__init__()
        print('in B init')

    def f2(self):
        # self.f1() or super.f1() both way use to call parent methods
        print('f2 works')


ob1 = A()
ob1.f1() # first work the init then the method
ob2 = B()
ob2.f2() # when B inherit from A first check B have init define if so then go to init first then call the method, if not then we check parent class A init 

# to call the parent class init we can use super()
ob2.f2() # init work only one time so when we call it second time its only call the method











