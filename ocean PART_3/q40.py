'''
Write a function that displays the spiral: RULLDDRRRUUULLLL… and so on. 
It should keep displaying until it has displayed 1,000,000 Letters in this pattern. (5 points)
'''

def spiral():
    s=''
    a=1
    b=2
    while len(s)<=1000000:
        s+='R'*a+'U'*a+'L'*b+'D'*b
        a+=2
        b+=2
    return s[0:1000000]
print(spiral())
print(len(spiral()))