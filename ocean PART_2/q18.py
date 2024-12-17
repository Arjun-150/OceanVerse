'''
 Fibonacci Sequence : 
 Write a program that prints the first n numbers in Fibonacci numbers (1 point).
'''

n=int(input('how many terms of the fibonacci sequence do you want : '))
a=0
b=1
l=[a,b]
c=0
while len(l)<n:
    c=l[-1]+l[-2]
    l.append(c)
for i in l:
    print(i,end=' ,')