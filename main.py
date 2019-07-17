#import python random module
#to generate random string
import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pwdlen = int(input('Desired Password Length: '))
pwdnums = int(input('Number of Passwords to Generate: '))

for pn in range(pwdnums):
    password = ''
    for pl in range(pwdlen):
        password += random.choice(chars)
    print(password)