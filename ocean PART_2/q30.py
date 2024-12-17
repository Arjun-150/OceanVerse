'''
Write a program that finds the gcd of two numbers using Euclid's Algrorithm. Given k
 as an input, display those two numbers, both with k
 digits, such that they take the maximum number of steps to find the GCD, across all the pair 
 of numbers, both of which are of k digits (8 points).
'''

n1=int(input('Enter 1st no: '))
n2=int(input('Enter 2nd no: '))
#using euclid's algorithm
#divide numbers and then further divide remainder and smaller number till 0 shows up. 
#there, the number other than zero is divisor  

while n2>0:
    n1,n2=n2,n1%n2
print(n1,'is GCD of given numbers')
