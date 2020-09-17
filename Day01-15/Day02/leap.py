"""
Enter the year, if it is a leap year, output True, otherwise output False
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

year = int(input('Please enter the year: '))
is_leap = (year %4 == 0 and year % 100 != 0 or year %400 == 0)

print(is_leap)