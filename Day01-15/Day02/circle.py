"""
Enter the radius to calculate the circumference and area of the circle
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

import math

radius = float(input("Please enter the radius of the circle:"))

perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('perimeter: %.2f' % perimeter)
print('area: %.2f' % area)