"""
Print various triangle patterns
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
Version: 0.1
Author: Thanhtv
Date: 2020-09-17
"""

row = int(input('Please enter the number of rows: '))

for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(2 * row - 1):
        if j < row - i - 1 or j > row -1 + i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
