"""
Find the number of all daffodils between 100~999
The number of daffodils is the sum of each cube equal to the number itself
For example: 153 = 1**3 + 5**3 + 3**3
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

def check_number(number):
    total = 0
    num = number
    while True:
        surplus = num % 10
        if surplus <= 0:
            break
        
        total += surplus ** 3
        num = num // 10
    
    if total == number:
        return True
    else:
        return False

for num in range(100, 1000):
    if check_number(num):
        print(num)
