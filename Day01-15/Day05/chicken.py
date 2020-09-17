"""
Solve the "Hundred Money and Hundred Chickens" problem
1 cock 5 yuan, 1 hen 3 yuan, 3 chicks 1 yuan, buy 100 chickens for 100 yuan
Ask how many rooster, hen and chicks there are
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('Rooster: %d, hen: %d, chick: %d'% (x, y, z))