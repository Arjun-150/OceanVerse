'''
Leap Year or Not: Write a program that checks if a given year is a leap year or not. 
Google for the details on how to figure out if the given number is a leap year or not. 
It is more complicated than simply checking for a multiple of 4 (1 point).
'''

y=int(input('Enter an year:'))
leap=True
if y%4==0:
    if y%100==0:
        if y%400!=0:
            leap=False
else:
    leap=False
if leap==True:
    print('It is a leap year')
else:
    print('It is not a leap year')