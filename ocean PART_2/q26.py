'''
Divisible by 7 and 5: Write a program that checks if a number provided by the user 
is divisible by both 7 and 5. Generalize it to a and b (1 point).
'''

n=int(input('enter the number : '))
a=int(input('divisibility check for the number1 : '))
b=int(input('divisibility check for the number2 : '))
if n%a==0:
    if n%b==0:
        print(n,'is divisible by both',a,'and',b)
    else:
        print(n,'is only divisible by',a,'and not',b)
else:
    if n%b==0:
        print(n,'is only divisible by',b,'and not',a)
    else:
        print(n,'is not divisible by both',a,'and',b)