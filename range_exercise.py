"""
---------------------------------------
# 1. Write a Python program to iterate over a range of numbers and print them.
---------------------------------------
for i in range(1,21):
    print(i)

---------------------------------------
# 2. Write a Python program to find the sum of all numbers in a range.
---------------------------------------
sumrange = sum(range(11))
print(sumrange)

---------------------------------------
# 3. Write a Python program to print all even numbers in a given range.
---------------------------------------
for i in range(1,21):
    if i % 2 == 0:
        print(i)

---------------------------------------
# 4. Write a Python program to print all odd numbers in a given range.
---------------------------------------
for i in range(1,21):
    if i % 2 == 1:      #or i % 2 != 0
        print(i)

---------------------------------------
# 5. Write a Python program to find the average of all numbers in a range.
---------------------------------------
given_range = range(1,48)
average = sum(given_range)/len(given_range)
print('Average of given range is: ',average)

---------------------------------------
# 6. Write a Python program to check if a number is present in a given range.
---------------------------------------
given_range = range(1,48)
num = int(input('Enter number to check: '))
print('Is number present in range? --> ',num in given_range)

---------------------------------------
# 7. Write a Python program to reverse a range of numbers and print them.
---------------------------------------
given_range = range(1,48)
rev_range = list(reversed(given_range))
for i in rev_range:
    print(i)

---------------------------------------
# 8. Write a Python program to find the product of all numbers in a range.
---------------------------------------
given_range = range(1,8)
res = 1
for i in given_range:
    res = res * i
print('product of all numbers in a range: ',res)

---------------------------------------
# 9. Write a Python program to print the squares of all numbers in a range.
---------------------------------------
given_range = range(1,21)
for i in given_range:
    print(i,'-->',i*i)

---------------------------------------
# 10. Write a Python program to print the cube of all numbers in a range.
---------------------------------------
given_range = range(1,21)
for i in given_range:
    print(i,'-->',i*i*i)
"""
