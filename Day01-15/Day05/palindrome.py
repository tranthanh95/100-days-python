"""
Determine whether the input positive integer is a palindrome
The number of palindrome refers to the number of a positive integer arranged from left to right and arranged from right to left.
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""


def check_palindrome(number):
    num = number
    total = 0

    while True:
        surplus = num % 10
        if surplus <= 0:
            break
        total = total * 10 + surplus
        num = num // 10

    if total == number:
        return True
    else:
        return False

num = int(input('Please enter a positive integer: '))

if check_palindrome(num):
    print('%d is the number of palindrome'% num)
else:
    print('%d is not the number of palindrome'% num)



