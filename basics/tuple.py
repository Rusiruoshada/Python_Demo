# use tuple for immutable values not like list (can't change value like getting index and assign new value num[3]=23 -> can't do this)
# to use a tuple we don't use [] for it use () or without any brackets

num = 12,32,42,'helo'
tup = (12,32,'rew')
tuple = [12,32,'wel']

print(type(tuple))
print(type(num))
print(type(tup))
print(len(num))

# unpacking list or tuple
n,n1,n2 = tup
m,m1,m2 = tuple

print(n,n1,n2)
print(m,m1,m2)

print(34 in num) # output is it in the tuple(boolean)

t = (45) # type show as int => because only 1 value in there
t1 = (45,) # now its show tuple

print(type(t))
print(type(t1))