"""
String common operations
Version: 0.1
Author: Thanhtv
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('The length of the string is:', len(str1))
print('Capitalize the first letter of a word: ', str1.title())
print('String becomes uppercase: ', str1.upper())

print('Is the string uppercase: ', str1.isupper())
print('Does the string start with hello: ', str1.startswith('hello'))
print('Does the string end with hello: ', str1.endswith('hello'))
print('Does the string start with an exclamation point: ', str1.startswith('!'))
print('Is the string ending with an exclamation point: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)