'''
Decimal to Binary Conversion: Write a program that converts a decimal number to its binary 
representation using loops, without using built-in conversion functions (1 point).
'''

n=int(input('enter the number : '))
m=n
bin=[]
pow=[]
while n!=0:
    l=[]
    for i in range(n):
        if n>=2**i:
            l.append(i)
        else:
            continue
    pow.append(max(l))
    n=n-2**(max(l))
a=max(pow)
for i in range(-1,-(a+2),-1):
    if -i-1 in pow:
        bin.insert(i,1)
    else:
        bin.insert(i,0)
result=''
for i in bin:
    result=result+str(i)
print('the binary code for',m,' = ',result)





