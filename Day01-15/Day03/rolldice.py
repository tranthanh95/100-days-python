"""
Roll the dice to decide what to do
Version: 0.1
Author: thanhtv
Date: 2020-09-18
"""

from random import randint

face = randint(1, 6)

if face == 1:
    result = 'sing a song'
elif face == 2:
    result = 'do a dance'
elif face == 3:
    result = 'learn to bark'
elif face == 4:
    result = 'Do push-ups'
elif face == 5:
    result = 'read tongue twister'
else:
    result = 'tell a cold joke'

print(result)
