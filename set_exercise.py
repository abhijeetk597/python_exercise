"""
---------------------------------------
# 1. Write a Python program to find the union of two sets.
---------------------------------------
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
unions1s2 = s1.union(s2)
print(unions1s2)

---------------------------------------
# 2. Write a Python program to find the intersection of two sets.
---------------------------------------
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
intersects1s2 = s1.intersection(s2)
print(intersects1s2)

---------------------------------------
# 3. Write a Python program to check if a set is a subset of another set.
---------------------------------------
s1 = {1,2,3,4,5}
s2 = {4,5}
s3 = {6,7,8}
print(s2.issubset(s1))
print(s3.issubset(s1))

---------------------------------------
# 4. Write a Python program to remove duplicate elements from a set.
---------------------------------------
s1 = {1,2,3,4,5,5,4,6,7,1,9,2}
print(s1)       #output--> {1, 2, 3, 4, 5, 6, 7, 9} .: Hence, set contains only unique elements

---------------------------------------
# 5. Write a Python program to add an element to a set.
---------------------------------------
s1 = {1,2,3,4,5}
#to add element 8 into s1
s1.add(8)
print(s1)       #output--> {1, 2, 3, 4, 5, 8}

---------------------------------------
# 6. Write a Python program to remove an element from a set.
---------------------------------------
s1 = {1,2,3,4,5}
#to remove 4 from s1
s1.discard(4)
print(s1)       #output--> {1, 2, 3, 5}

---------------------------------------
# 7. Write a Python program to find the difference between two sets.
---------------------------------------
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
diff = s1 - s2
print('Difference in s1 and s2 is : ', diff)

---------------------------------------
# 8. Write a Python program to check if two sets are disjoint.
---------------------------------------
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print('Are s1 & s2 disjoint: ', s1.isdisjoint(s2))

---------------------------------------
# 9. Write a Python program to find the symmetric difference between two sets.
---------------------------------------
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print('Symmetric difference: ', s1.symmetric_difference(s2))

---------------------------------------
# 10. Write a Python program to check if a set is empty.
---------------------------------------
s1 = {1,2,3,4,5}
if not s1:
    print('Set is empty')
else:
    print('Set is not empty')
"""
