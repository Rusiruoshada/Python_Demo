# python mainly have while and for loop
# for loop work as for each(no condition check)
# while
a = 10
while a<20:
    print('use while loop');
    a +=1

# nested while
b = 0;
while b<10:
    # in print method its have end parameter its usually set to '\n' (new line). we can change it
    print("hello", end = ' ')
    j=0
    while j<5:
        print(" o kawai koto!",end=' ')
        j += 1
    print()
    b +=1

# for loop
c = [2,'roms',3.2,None,True,'python']
cSize = len(c)

print('',end='[')
for val in c:
    print(val,end=', ')

print('',end=']\n')
# output: [2, roms, 3.2, None, True, python, ]

# for loop for dict
d = {'a':2,'b':4,'c':5,'d':0,'e':32}
for k,v in d.items():
    print(k,": ",v)

# for loop for tuple
e=(12,'key',123,2.3,'hello')
for val in e:
    print(val,end=' ,')