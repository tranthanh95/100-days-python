"""
Convert Fahrenheit to Celsius
F = 1.8C + 32
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

f = float(input('Please enter the temperature in Fahrenheit: '))
c = (f - 32) / 1.8
print('%.1fFahrenheit = %.1fCelsius' % (f, c))