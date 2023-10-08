"""
# 1. Write a Python program to check if a number is positive, negative, or zero.
num = int(input('Enter number to check: '))
if num < 0:
    print('Entered Number', num, 'is negative.')
elif num > 0:
    print('Entered Number', num, 'is positive.')
else:
    print('Entered Number is zero.')

# 2. Write a Python program to check if a number is even or odd.
num = int(input('Enter number to check if even or odd: '))
print('Entered number is even' if num % 2== 0 else 'Entered number is odd')

# 3. Write a Python program to check if a year is a leap year or not.
num = int(input('Enter year: '))
if num % 400 == 0:
    print(num, 'is a leap year.')
elif num % 4 == 0 and num % 100 != 0:
    print(num, 'is a leap year.')
else:
    print(num, 'is not a leap year.')

# 4. Write a Python program to find the maximum of three numbers using if-else.
x,y,z = map(int,input('Enter 3 numbers (space separated): ').split())
max = x
if y > x:
    max = y
if z >= y and z > x:
    max = z
print('Maximum number is: ',max)

# 5. Write a Python program to check if a number is prime.
def isPrime(n):
    if n < 2:
        return 'Entered number is not Prime'
    if n == 2:
        return 'Entered number is Prime'
    i = 2
    while i*i <= n:
        if n % i == 0:
            return 'Entered number is not Prime'
        i += 1
    return 'Entered number is Prime'
num = int(input('Enter number: '))
print(isPrime(num))

# 6. Write a Python program to check if a number is divisible by both 3 and 5.
num = int(input('Enter number: '))
if num % 3 == 0 and num % 5 == 0:
    print('Entered number is divisible by both 3 and 5')
else:
    print('Entered number is not divisible by both 3 and 5')

# 7. Write a Python program to check if a character is a vowel or consonant.
char = input('Enter character: ')
char = char.lower()
if char.isalpha():
    if char in ['a','e','i','o','u']:
        print('Entered character is vowel.')
    else:
        print('Entered character is consonant.')
else:
    print('Entered character is not not an alphabet.')

# 8. Write a Python program to check if a given string is a palindrome using if-else.
string = input('Enter string: ')
if string == string[::-1]:
    print('Entered string is palindrome')
else:
    print('Entered string is not palindrome')

# 9. Write a Python program to determine the largest among three numbers using nested if-else.
x,y,z = map(int,input('Enter 3 numbers (space separated): ').split())
max = x
if y > x:
    max = y
    if z >= y and z > x:
        max = z
elif x > y:
    if z > x:
        max = z
else:
    if z > x:
        max = z
print('Maximum number is: ',max)

# 10. Write a Python program to check if a triangle is equilateral,
# isosceles, or scalene based on its side lengths using if-else.
x,y,z = map(int,input('Enter 3 sides of triangle (space separated): ').split())
if x < y + z and y < x + z and z < x + y:
    if x == y == z:
        print('It is a equilateral triangle')
    if x == y or y == z or x == z:
        print('It is a isosceles triangle')
    else:
        print('It is a scalene triangle')
else:
    print("Entered sides doesn't form a triangle.")
"""