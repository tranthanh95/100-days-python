"""
Use a for loop to achieve the sum of even numbers between 1 and 100
Version: 0.1
Author: Thanhtv
Date: 2020-09-01
"""

sum = 0
for item in range(2, 101, 2):
    print(item)
    sum += item

print('sum = ', sum)
