'''
Write a program that counts and prints the number of vowels 
and the number of consonants in the string (1 point)
'''

s=input('enter the string : ')
vowels=['a','e','i','o','u','A','E','I','O','U']
v=0
c=0
for i in s:
    if i in vowels:
        v+=1
    else:
        c+=1
print('the number of vowels = ',v)
print('the number of consonants = ',c)


