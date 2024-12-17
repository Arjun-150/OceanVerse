'''
Given a string, check if it is a palindrome or not (1 point).
'''

def palicheck(s):
    if s==s[::-1]:
        print(s, 'is a palindrome')
    else:
        print(s, 'is not a palindrome')
s=input('enter the string : ')
palicheck(s)