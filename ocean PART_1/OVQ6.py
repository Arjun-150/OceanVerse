'''
Write a program to take as input a number n
 and display the first n
 natural numbers (1 point).
'''

n=int(input('enter a number : '))
for i in range(n):
    print(1+i, end=" ")