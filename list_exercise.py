"""
# 1. Write a Python program to find the sum of all elements in a list.
def sumall(list):
    return sum(list)
# list = [1,2,3,4]
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('Sum of all list elements is: ',sumall(list))

# 2. Write a Python program to find the maximum and minimum elements in a list.
def maxmin(list):
    return (max(list),min(list))
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('Max and Min element are: ',maxmin(list))

# 3. Write a Python program to remove duplicates from a list.
def removedup(list):
    res = []
    for element in list:
        if element not in res:
            res.append(element)
        else:
            continue
    return res
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('Here is list after removing duplicates: ',removedup(list))

# 4. Write a Python program to check if a list is sorted in ascending order.
def ifsortedasc(list):
    print(sorted(list))
    print(list)
    return list == sorted(list)
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('whether list is sorted or not: ', ifsortedasc(list))

# 5. Write a Python program to find the second largest element in a list.
def seclargest(list):
    temp = sorted(set(list))
    if len(temp) == 1:
        return -1
    return temp[-2]
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('Second largest element in list is: ', seclargest(list))

# 6. Write a Python program to sort a list of strings in alphabetical order.
def sortstrings(list):
    return sorted(list)
list = list(map(str,input('Enter list of strings (comma separated):').split(',')))
print('Sorted list of string is: ', sortstrings(list))

# 7. Write a Python program to find the common elements between two lists.
def intersection(l1,l2):
    return set(l1).intersection(set(l2))
l1 = [1,2,3,4,5,6]
l2 = [2,3,8,9,15,5]
print('Common elements are: ',*intersection(l1,l2))

# 8. Write a Python program to remove the nth occurrence of an element from a list.
list = [1,2,3,4,5,1,2,4,8,6,9,7,1,6]
element = 2
occur = 2
index = None
for i in range(len(list)):
    if list[i] == element:
        occur -= 1
    if occur == 0:
        index = i
        break
del(list[index])
print(list)

# 9. Write a Python program to find the difference between two lists.
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40]
temp = [x for x in li1 if x not in li2]
print('Difference list1 & list2 is : ', temp)

# 10. Write a Python program to remove the elements of a list that are divisible by 3.
list = list(range(50))
res = [x for x in list if x%3 != 0]
print(res)
"""