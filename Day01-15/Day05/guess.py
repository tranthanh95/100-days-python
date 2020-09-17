"""
Guess the number game
The computer produces a random number between 1 and 100, and the human guesses it
The computer will give hints according to the number guessed by the person.
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('Please enter:'))
    if number < answer:
        print('bigger')
    elif number > answer:
        print('smaller')
    else:
        print('Congratulations, you guessed it!')
        break
print('You guessed %d times in total'% counter)

if counter > 7:
     print('Your IQ balance is obviously insufficient')
