"""
Determine whether the input side length can form a triangle
If so, calculate the perimeter and area of the triangle
Version: 0.1
Author: Thanhtv
Date: 2020-09-18
"""

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('Circumference: %f'% (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print('Area: %f'% (area))
else:
    print('Cannot form a triangle')



