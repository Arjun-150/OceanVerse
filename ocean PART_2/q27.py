'''Create a Python program that prompts the user for their age. If the age is less than 18, 
print “You are a minor.” If the age is between 18 and 65, print “You are an adult.” Otherwise, 
print “You are a senior citizen.” (1 point).
'''

age=int(input('enter your age : '))
if age<18:
    print('you are a minor')
elif 18<age<65:
    print('you are an adult')
else:
    print('you are a senior citizen')
    