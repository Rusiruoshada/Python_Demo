#there is a stroy about duck typing it say duck cuk, but if the crow also cuk we consider crow as a duck too

class lap:
    def build(self):
        print('lap builds')

class desktop:
    def build(self):
        print('desktop builds')

class tablet:
    def openApp(self):
        print('open apps')
    
class devs:
    def code(self,machine:lap):
        print('coding')
        machine.build()

ob0 = lap()
ob1 = desktop()
ob2 = tablet()

ob3 = devs()
ob3.code(ob0)
ob3.code(ob1) # even though desktop obj not a laptop type its call build method

    