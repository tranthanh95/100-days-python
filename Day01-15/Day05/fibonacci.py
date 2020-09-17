"""
Output the first 20 numbers of the Fibonacci sequence
1 1 2 3 5 8 13 21 ...
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

a = 0
b = 1
for _ in range(20):
    b, a = a + b, b
    print(a, end=' ')
