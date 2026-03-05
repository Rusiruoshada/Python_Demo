num = [2,3,4,5,6,7,4,2,45,4]
num1 = ['nav',32,3.23]
mix = [num,num1]

#num slice
print(num[2:5])

print(num.append(33)) # add value to end
print(num)
print(num.count(4)) # count how many appear in the list
num.insert(1,9) # add the value in given index (index, value)
print(num)
num.remove(45)
print(num)
print(num.pop(3)) # pop work like stack(index 0), pop given index
del num[7:] # use del to delete multiple values in list
print(num)
num.extend([10,11,12,121])
print(num) # use extend to add more element at once at the end
num.reverse()
print(num)
num.sort() # default ASC
print(num)
print(min(num))
print(max(num))
print(sum(num)) # get the sum
print(type(num)) # <class 'list'>
