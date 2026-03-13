# threads can do using classes or functions
# use this for run code parallel(simultaneously)
# process have multiple threads

from threading import Thread

class hello(Thread):
    def run(self): # run() contains the actual work the thread should perform.
        for i in range(5):
            print("hello", i+1)

class hi(Thread):
    def run(self): #
        for i in range(5):
            print("hi", i+1)

t1 = hello()
t2 = hi()

# python runs line by line so first finish the t1.do then t2.do
# to use thread have to start() this will call the run()
t1.start()
t2.start()

# to do it using functions
def greet():
    for i in range(0,5):
        print("Youkosho, wathashiwa solo society")

def greetBack():
    for i in range(0,5):
        print('onegaisimas!')


t3 = Thread(target=greet)
t4 = Thread(target=greetBack)

t3.start()
t4.start()

# normally if we don't join the parallel bye also treat as a thread and not exactly run after everything
t1.join()
t2.join()
t3.join()
t4.join()

print('bye')
