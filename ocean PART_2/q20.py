'''
Write a piece of code which does exactly as specified in this video (10 points).
'''
# snake.py

n,c=int(input('Enter number of lines and curvature''\n')),float(input())
for i in range(n):
    print(int(((n-i)**2)*c)*' ','*')
for i in range(1, n+1):
    print(int((i**2)*c)*' ','*')