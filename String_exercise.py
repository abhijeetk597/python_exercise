# 1. Write a Python program to count the number of characters in a string.
"""
    def countchar(s):
        return len(s)
    s = input('Enter string to characters: ')
    print('There are',countchar(s),' characters in your string.')

# 2. Write a Python program to reverse a string.
    def rev_string(s):
        return s[::-1]
    s = input('Enter string to reverse: ')
    print('Reversed string is: ',rev_string(s))

# 3. Write a Python program to check if a string is a palindrome.
# solution 1
    def ifPalindrome(s):
        return s == s[::-1]
    s = input('Enter string: ')
    print('Palindrome status: ', ifPalindrome(s))

# solution 2
    def ifPalindrome(s):
        front = 0
        rev = len(s)-1
        while front < rev:
            if s[front] != s[rev]:
                return False
            front += 1
            rev -= 1
        return True
    s = input('Enter string: ')
    print('Palindrome status: ', ifPalindrome(s))

# 4. Write a Python program to remove all the vowels from a string.
def remove_vowels(s):
    temp = [i for i in s if i not in ['a','e','i','o','u','A','E','I','O','U']]
    return ''.join(temp)
s = input('Enter string: ')
print('String without vowels is: ',remove_vowels(s))

# 5. Write a Python program to find the first non-repeating character in a string.
def firstnonrepeat(s):
    s = s.lower()
    temp = [i for i in s if s.count(i)==1]
    return temp[0] if temp else -1
s = input('Enter string: ')
print(firstnonrepeat(s))

# 6. Write a Python program to capitalize the first letter of each word in a string.
def capfirstletter(s):
    return s.title()
s = input('Enter string: ')
print(capfirstletter(s))

# 7. Write a Python program to check if a string is an anagram of another string.
def if_anagram(s1,s2):
    return sorted(s1.lower()) == sorted(s2.lower())
s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
print(if_anagram(s1,s2))

# 8. Write a Python program to find the most frequent character in a string.
def mostfreqchar(s):
    s = s.lower()
    dict1 = {char:s.count(char) for char in set(s) if char != ' '}
    maxfreq = max(dict1.values())
    frqchar = []
    for key,value in dict1.items():
        if value == maxfreq:
            frqchar.append(key)
    return frqchar
s = input('Enter string: ')
print('Most frequent characters in given string is/are: ', *mostfreqchar(s))

# 9. Write a Python program to check if a string is a valid email address.
def ifvalidemail(s):
    if '@' in s and '.' in s.split('@')[1]:
        username = s.split('@')[0]
        domain = s.split('@')[1]
        cond1 = username.isalnum()
        cond2 = domain.split('.')[0].isalnum()
        cond3 = domain.split('.')[1].isalpha()
        if cond1 and cond2 and cond3:
            return 'Valid E-mail'
    return 'Invalid E-mail'
s = input('Enter e-mail ID to validate: ')
print(ifvalidemail(s))

# 10. Write a Python program to find the length of the longest substring without repeating characters.
string = 'Lorem ipsum dolor sit amet consectetur adipisicing elit Ad doloremque consectetur maiores nam libero \
            quibusdam delectus debitis eligendi sit explicabo exercitationem expedita laborum illum inventore'
list = string.split(' ')
res = -1
res_word = ''
for word in list:
    if len(word) > res and len(word) == len(set(word)):
        res = len(word)
        res_word = word
print('Length of the longest substring without repeating characters: ', res,'- for word -->', res_word)
"""