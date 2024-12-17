'''
Write a program to find out if the given number is prime or not (1 point)
'''

n=int(input('enter the number :'))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
    else:
        continue
if len(l)==2:
    print(n ,'is a prime number')
else:
    print(n ,'is not a prime number')
    