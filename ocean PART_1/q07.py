a=int(input('enter the first term of your arithmetic series : '))
d=int(input('enter the common difference :'))
b=int(input('enter the highest possible term of your series :'))

while a<b:
    print(a, end=' ')
    a+=d
