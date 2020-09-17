"""
Use the while loop to achieve the sum of even numbers between 1 and 100
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

sum, num = 0, 2
while num <= 100:
    sum += num
    num += 2

print('sum = ', sum)
