'''
Positive or Negative: Write a program that asks the user for a number and prints 
whether the number is positive, negative, or zero (1 point).
'''

n=int(input('enter the number : '))
if n<0:
    print(n, 'is negative')
elif n==0:
    print(n, 'is zero')
else:
    print(n, 'is positive')