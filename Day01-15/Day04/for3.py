"""
Enter a non-negative integer n to calculate n!
Version: 0.1
Author: thanhtv
Date: 2020-09-17
"""

n = int(input('n = '))

result = 1
for item in range(1, n +1):
    result *= item
    pass


print('result = ', result)
