'''
Checking for Even or Odd: Write a function called is_even that takes an integer and 
returns True if the number is even, and False if it is odd. (1 point)
'''

def is_even(n):
    if n%2==0:
        return bool(1)
    else:
        return bool(0)
n=int(input('enter the number : '))
print(is_even(n))
