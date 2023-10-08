"""
# 1. Write a Python program to print the numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# 2. Write a Python program to calculate the sum of all numbers in a list using a for loop.
list1 = list(range(11))
res = 0
for i in list1:
    res += i
print('Sum of all numbers in list is: ', res)

# 3. Write a Python program to find the factorial of a number using a for loop.
def factorial(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(2,n+1):
        res *= i
    return res
num = int(input('Enter number for getting factorial: '))
print('Factorial of',num,'is',factorial(num))

# 4. Write a Python program to print all the even numbers between 1 and 50 using a for loop.
for i in range(1,51):
    if i % 2 == 0:
        print(i)

# 5. Write a Python program to iterate over a string and print each character using a for loop.
string = input('Enter string: ')
for i in string:
    print(i)

# 6. Write a Python program to iterate over a list of tuples and print each element using a for loop.
list = [(1,2),(3,5),(2,5),(3,6),(7,8)]
for i in list:
    for j in i:
        print(j)

# 7. Write a Python program to find the largest element in a list using a for loop.
def find_largest(list):
    if not list:
        return 'List is empty'
    largest = -999999
    for i in list:
        if i > largest:
            largest = i
    return 'Largest element is :', largest
list = [999, 147, 450, 451, 283, 397, 472, 299, 225, 33, 392, 53, 203, 45, 309, 288, 465, 48, 350, 423, 20, 355, 299]
print(*find_largest(list))

# 8. Write a Python program to check if all elements in a list are even using a for loop.
def check_even(list):
    if not list:
        return 'List is empty'
    for i in list:
        if i % 2 != 0:
            return 'All elements in a list are not even'
    return 'All elements in list are even.'
list = [1]
print(check_even(list))

# 9. Write a Python program to find the common elements between two lists using a for loop.
list1 = [1,2,3,3,3,4,5,6]
list2 = [2,3,25,5,7,15]
temp = []
for i in set(list1):
    for j in set(list2):
        if i == j:
            temp.append(i)
print('Common elements are: ', *temp)

# 10. Write a Python program to calculate the sum of the digits of a number using a for loop.
num = int(input('Enter number: '))
digit_sum = 0
for i in str(num):
    digit_sum += int(i)
print('Sum of digits: ',digit_sum)
"""