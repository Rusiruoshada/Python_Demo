#  set is a collection of unique unordered ele
# set not store base on the value its use hash value
# use {} to sets

num = {12,3,'hel',90,3}

print(num) # only show unique values so , end 3 not showing -> {90, 3, 12, 'hel'}
print(type(num)) # <class 'set'>

# creating a empty set
a = {} # this will show as type dict(dictionary)
a1 = set()

print(type(a))
print(type(a1))

set1 = set('abcdmnop')
set2 = set('aeioupd')

print(set1)
print(set2)

print(set1 - set2) # show only in set1
print(set1 | set2) # all value
print(set1 & set2) # common values
print(set1 ^ set2) # exclude common value only show set1 and set2 unique value