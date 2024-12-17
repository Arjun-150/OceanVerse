'''
Finding the Maximum: Write a function called find_max that takes a list of numbers 
and returns the largest number in the list. (1 point)
'''

def find_max(l):
    m=0
    for i in l:
        if i>m:
            m=i
        else:
            continue
    return m
l=[]
n=int(input('how many elements do you want in your list : '))
for i in range(n):
    a=int(input('enter number : '))
    l.append(a)
print('the largest number in the list is',find_max(l))