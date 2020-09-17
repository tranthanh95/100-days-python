"""
Enter a positive integer to determine if it is a prime number
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

from math import sqrt

num = int(input('Please enter a positive integer: '))
end = int(sqrt(num))
is_prime = True

for item in range(2, end + 1):
    if num % item == 0:
        is_prime = False
        break
    pass

if is_prime and num != 1:
    print('%d is a prime number'% num)
else:
     print('%d is not a prime number'% num)
