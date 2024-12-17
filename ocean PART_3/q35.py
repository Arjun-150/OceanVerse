'''
Write a function called fibonacci that takes an integer n and returns 
the n-th number in the Fibonacci sequence. (1 point)
'''

def fibo(n):
    a=0
    b=1
    L=[a,b]
    while len(L)<n:
        c=L[-1]+L[-2]
        L.append(c)
    return L[-1]

n=int(input('enter the number : '))
print('the n-th number in the fibonacci sequence is', fibo(n))