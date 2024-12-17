'''
 Write a program to take as input n and 
 print all prime numbers upto and including n (1 point)
 '''

n=int(input('enter the number :'))
l=[]
for i in range(3,n+1):
    p=[]
    for j in range(1,i+1):
        if i%j==0:
            p.append(j)
        else:
            continue
    if len(p)==2:
        l.append(i)
    else:
        continue
for a in l:
    print(a,end=' ,')
