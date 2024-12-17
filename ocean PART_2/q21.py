'''
Factorial: Write a program that calculates the factorial of a number 
provided by the user (1 point).
'''

n=int(input('enter the number : '))
f=1
for i in range(1,n+1):
    f=f*i
print('the factorial of ',n,' = ',f)