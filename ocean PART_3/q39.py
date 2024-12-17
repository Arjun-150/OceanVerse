'''
Calculate Area of a Circle: Write a function called circle_area that takes the radius  
of a circle as an argument and returns its area. (1 point)
'''

import math

def circle_area(r):
    area=math.pi*r*r
    return area

r=int(input('enter the radius of the circle : '))
print('the area is', circle_area(r), 'sq. units')