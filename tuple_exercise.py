"""
---------------------------------------
# 1. Write a Python program to find the length of a tuple.
---------------------------------------
tup = (1,2,3,4,5,6,7,8,9)
print('length of tuple is: ',len(tup))

---------------------------------------
# 2. Write a Python program to concatenate two tuples.
---------------------------------------
tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
tup3 = tup1 + tup2
print(tup3)

---------------------------------------
# 3. Write a Python program to convert a tuple to a list.
---------------------------------------
tup = (1,2,3,4)
list = list(tup)
print(list)

---------------------------------------
# 4. Write a Python program to find the index of an element in a tuple.
---------------------------------------
tup = (1,4,7,2,5,8,3,6,9)
print(tup.index(2))

---------------------------------------
# 5. Write a Python program to check if an element exists in a tuple.
---------------------------------------
tup = (1,4,7,2,5,8,3,6,9)
element = int(input('Enter integer to search: '))
print('Element is present' if element in tup else 'Element is not in tuple.')

---------------------------------------
# 6. Write a Python program to count the number of occurrences of an element in a tuple.
---------------------------------------
tup = (1,4,7,2,5,8,3,6,9,1,5,9,7,5,3,4,5,8,6,2,17,7,8,9,24,7,6,3)
n = int(input('Enter integer to count the number of occurrences: '))
if n in tup:
    print(n, 'occurs', tup.count(n), 'times in tuple')
else:
    print('Entered number is not in tuple')

---------------------------------------
# 7. Write a Python program to find the maximum and minimum elements in a tuple.
---------------------------------------
tup = (1,4,7,2,5,8,3,6,9,1,5,9,7,5,3,4,5,8,6,2,17,7,8,9,24,7,6,3)
print('Maximum and minimum numbers in tuple are: ', (max(tup),min(tup)))

---------------------------------------
# 8. Write a Python program to reverse a tuple.
---------------------------------------
tup = (1,4,7,2,5,8,3,6,9,1,5,9,7,5,3,4,5,8,6,2,17,7,8,9,24,7,6,3)
rev_tuple = tuple(reversed(tup))
print(rev_tuple)

---------------------------------------
# 9. Write a Python program to check if all elements in a tuple are the same.
---------------------------------------
tup = (1,4,7,2,5,8,3,6,9,1,5,9,7,5,3,4,5,8,6,2,17,7,8,9,24,7,6,3)
tup2 = (2,2,2,2,2,2,2,2,2,2,)
print('tup:','All elements in tuple are same' if len(set(tup)) == 1 else 'Tuple contains different elements')
print('tup2:','All elements in tuple are same' if len(set(tup2)) == 1 else 'Tuple contains different elements')

---------------------------------------
# 10. Write a Python program to create a new tuple with the elements from two existing tuples.
---------------------------------------
tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
tup3 = tup1 + tup2
print(tup3)
"""
