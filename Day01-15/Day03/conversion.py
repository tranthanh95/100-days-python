"""
The imperial unit inch and the metric unit centimeter are interchanged
Version: 0.1
Author: Thanhtv
Date: 2020-09-18
"""

value = float(input('Please enter the length:'))

unit = input('Please enter the unit:')

if unit == 'in' or unit == 'inch':
    print('%f inch = %f cm'% (value, value * 2.54))
elif unit == 'cm' or unit == 'cm':
    print('%f cm = %f inch'% (value, value / 2.54))
else:
    print('Please enter a valid unit')
