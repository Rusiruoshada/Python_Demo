# hide unnecessary information from the user
# abc -> abstract base class
# can't make obj from abstract class
# to be a abstract we have to inherit from the ABC
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self): pass

class paymentGateway(ABC):
    @abstractmethod
    def pay(): pass

# when we use abstract class we have to implement the abstract methods
class paypal(paymentGateway):
    def pay(self):
        print('paying using paypal')

class purchase:
    def __init__(self,gateway):
        self.gateway = gateway

    def checkout(self):
        print('checkout>>')

        self.gateway.pay()

gateway1 = paypal()
purchase = purchase(gateway1)

purchase.checkout()



