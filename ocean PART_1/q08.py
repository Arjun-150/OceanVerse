'''
Write a program that calculates and prints the sum of all numbers from 1 to n,
where n is provided by the user (1 point).
'''

n=int(input('enter the number : '))
s=0
for i in range(1,n+1):
    s+=i
print('the sum of all numbers from 1 to n =', s)
