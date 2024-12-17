'''
Simple Interest Calculation: Write a program that calculates the simple interest 
for given principal, rate, and time provided by the user (1 point).
'''

p=int(input('enter the principal amount : '))
r=int(input('enter the rate of interest in percentage : '))
t=int(input('enter the time period : '))
si=p*r*t/100
print('the simple interest is = ', si,)