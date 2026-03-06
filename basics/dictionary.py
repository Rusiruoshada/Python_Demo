#  to create dict we use {} and its key value pair data structure
#  unique(only keys), unordered 

data = {'h': 12,'o':32,3:'hello',3.2:32,'32':2.4}
print(data)

print(data['h']) # output: 12
print(data.get('h1','not found'))# output: not found
print(data.keys()) # output: dict_keys(['h', 'o', 3, 3.2, '32'])
print(data.values()) # output: dict_values([12, 32, 'hello', 32, 2.4])
print(data.pop('h'))

