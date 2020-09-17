"""
Output prime numbers between 2 and 99
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

import math
from math import sqrt

def check_prime(number):
    if number <= 1:
        return False
    
    # print(math.ceil(sqrt(number)))

    for index in range(2, math.ceil(sqrt(number)) + 1):
        if number % index == 0:
            return False

    return True

for num in range(2, 100):
    if check_prime(num):
        print(num)

# print(check_prime(25))