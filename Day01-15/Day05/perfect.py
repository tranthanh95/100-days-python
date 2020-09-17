"""
Find all perfect numbers between 1 and 9999
A perfect number is a number whose sum of all factors except itself is exactly equal to the number itself
For example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""


def check_number_perfect(number):
    total = 0
    for index in range(1, number):
        if number % index == 0:
            total += index

    return total == number

for num in range(1, 10000):
    if check_number_perfect(num):
        print(num)

