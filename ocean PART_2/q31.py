'''
Write a program to populate a list L with the first n natural numbers (1 point).
'''

n=int(input('enter the number : '))
L=[]
for i in range(1,n+1):
    L.append(i)
print(L)