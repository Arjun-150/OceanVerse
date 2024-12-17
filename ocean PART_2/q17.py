'''
List of Squares: Write a program that prints the square of numbers from 1 to n, 
where n is provided by the user (1 point).
'''

l=[]
n=int(input('enter the number : '))
for i in range(1,n+1):
    l.append(i**2)
for i in l:
    print(i, end=' ,')