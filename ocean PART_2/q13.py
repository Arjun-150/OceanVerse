'''
Take two strings of the same length and intersperse the second one into the first one:

Input:
india
super
Output:
isnudpiear
'''

def intersperse(a,b):
    s1=[]
    s2=[]
    l=[]
    for i in a:
        s1.append(i)
    for i in b:
        s2.append(i)
    s1=s1[::-1]
    s2=s2[::-1]
    for i in range(len(s1+s2)):
            if i%2==0:
                 l.append(s1.pop())
            else:
                 l.append(s2.pop())
    for i in l:
         print(i,end='')

a=input('enter string1 : ')
b=input('enter string2 : ')
intersperse(a,b)
