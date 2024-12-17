'''
Write a program that takes a number n from the user and prints the multiplication table 
for that number from 1 to 10. Generalize it from i
 to j
'''

n=int(input('Enter the number for which you want the multiplication table : '))
i=int(input('Enter i value :'))
j=int(input('Enter j value :'))
while i<=j:
    print(n,'X',i,'=',n*i)
    i+=1
