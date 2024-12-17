'''
Print Star Pattern: Write a program that takes a number n from the user and prints 
a right-angled triangle pattern with stars of n rows (1 point) .
'''

n=int(input('enter a number n:'))
for i in range(n):
    for j in range(n):
        if j<=i:
            print('*', end='')
        
        else:
            continue
    print('\n')