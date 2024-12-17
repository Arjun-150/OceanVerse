'''
Write a function called factorial that takes an integer n and returns the factorial of n. (1 point)
'''

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input('enter the number : '))
print('factorial is',fact(n))