"""
User authentication

Version: 0.1
Author: Thanhtv
Date: 2020-09-18
"""

import getpass
# from getpass import getpass
# from getpass import *

username = input('Please enter your username: ')
# password = input('Please enter your password: ')
# There is no echo in the terminal when entering the password
password = getpass.getpass('Please enter your password: ')
if username == 'admin' and password == '123456':
    print('Authentication is successful!')
else:
    print('Authentication failed!')
