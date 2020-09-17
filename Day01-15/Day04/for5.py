"""
Enter two positive integers to calculate the greatest common divisor and least common multiple
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('The greatest common divisor of %d and %d is %d'% (x, y, factor))
        print('The least common multiple of %d and %d is %d'% (x, y, x * y // factor))
        break
