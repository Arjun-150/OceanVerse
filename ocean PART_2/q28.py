'''
Grading System: Write a program that takes the marks of five subjects from the user and 
calculates the grade according to the average marks: A if average >= 90 B 
if average >= 80 and < 90 C if average >= 70 and < 80 D 
if average >= 60 and < 70 F otherwise (1 point).
'''

a=int(input('enter the marks of subject_1 : '))
b=int(input('enter the marks of subject_2 : '))
c=int(input('enter the marks of subject_3 : '))
d=int(input('enter the marks of subject_4 : '))
e=int(input('enter the marks of subject_5 : '))
avg=(a+b+c+d+e)/5
if avg>=90:
    grade='A'
elif avg>=80:
    grade='B'
elif avg>=70:
    grade='C'
elif avg>=60:
    grade='D'
else:
    grade='F'
print('Grade : ',grade)
