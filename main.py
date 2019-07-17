#import python random module
#to generate random string
import random

#by using a large number of characters
#we can create a much harder password
strchars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_*+=!@#$%^&'
len = int(input('Desired Password Length: '))
nums = int(input('Number of Passwords to Generate: '))
pwdlen = int(len)
pwdnums = int(nums)
"""
for pn in range(pwdnums):
    password = ''
    for pl in range(pwdlen):
        password += random.choice(chars)
    print(password)
"""
def pwdgen(pwdnums = 1, pwdlen = 8, chars = strchars):
#We will generate passwords with either parameters set by the user input
#or with default settings
    