
"""# 1. Write a Python program to iterate over a dictionary and print its keys and values.
dict1 = {i:i*i for i in range(1,11)}
print('key \t\t value')
for key,value in dict1.items():
    print(key,'\t\t\t',value)

# 2. Write a Python program to check if a key exists in a dictionary.
dict1 = {i:i*i for i in range(1,11)}
x = int(input('Enter number to check if present in dict keys: '))
if x in dict1.keys():
    print('Given number is a key in dictionary')
else:
    print('Given number is not a key in dictionary')

# 3. Write a Python program to get the value associated with a key in a dictionary.
dict1 = {i:i*i for i in range(1,11)}
print('Keys present in dictionary: ', list(dict1.keys()))
x = int(input('Enter a key to get value associated: '))
print('key', x,'value--> ',dict1[x])

# 4. Write a Python program to remove a key from a dictionary.
dict1 = {i:i*i for i in range(0,11)}
# to remove key 5
dict1.pop(5)
print(dict1)

# 5. Write a Python program to sort a dictionary by its values.**
dict1 = {1:'india', 2:'is', 3:'my', 4:'country', 5:'heritage', 6:'culture'}
dict2 = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(dict2)

# 6. Write a Python program to merge two dictionaries.
dict1 = {5:'india', 7:'is', 11:'my', 4:'country', 18:'heritage', 33:'culture'}
dict2 = {i:i*i for i in range(1,11)}
dict2.update(dict1.items())
print(dict2)

# 7. Write a Python program to count the frequency of each element in a dictionary.

# 8. Write a Python program to find the length of a dictionary.
dict1 = {5:'india', 7:'is', 11:'my', 4:'country', 18:'heritage', 33:'culture'}
print(len(dict1))

# 9. Write a Python program to check if a dictionary is empty.
dict1 = {5:'india', 7:'is', 11:'my', 4:'country', 18:'heritage', 33:'culture'}
dict2 = {}
print('Dictionary is empty' if len(dict1) == 0 else 'Dictionary is not empty')
print('Dictionary is empty' if len(dict2) == 0 else 'Dictionary is not empty')

# 10. Write a Python program to find the keys with the maximum and minimum values in a dictionary.
dict1 = {i:i*i for i in range(5,48)}
dmaxv = [k for k in dict1 if dict1[k] == max(dict1.values())]
dminv = [k for k in dict1 if dict1[k] == min(dict1.values())]
print('Key having max value is: ',*dmaxv)
print('Key having min value is: ',*dminv)
"""