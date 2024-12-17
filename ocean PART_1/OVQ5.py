'''
Understand how to use a if conditional in python.
print Ask the user to enter a number and check if the number is even or odd (1 point).
'''

def OddEven():
    number=int(input("enter a number:"))
    if number%2==0:
        print("the given number is even")
    else:
        print("the given number is odd")
    
    answer=input('do you want to check for another number: (y/n)')
    if answer=='y':
        OddEven()
    else:
        print('thank you')
OddEven()
