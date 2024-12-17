'''
Write a program to populate a list L with random numbers in the range 1 to 1000 (1 point).
'''

import random
l=[]
n=int(input('How many elements should the list have? '))     
for i in range(n):
    l.append(random.randint(1,1000))                         
print(l)

