#Pass-stor: created by Lee Baldwin


#import python random module
#to generate random string
from random import sample

#by using a large number of characters
#we can create a much harder password
strchars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_*+=!@#$%^&'

def pwdgen(pwdlen = 8, pwdnums = 1, chars = strchars):
#We will generate passwords with either parameters set by the user input
#or with default settings
    if pwdnums == 1:
        return ''.join(sample(chars, pwdlen))
    
    passwords = []
    while pwdnums > 0:
        passwords.append(''.join(sample(chars, pwdlen)))
        pwdnums -= 1

    return passwords

plen = input('Desired Password Length: ')
pnums = input('Number of Passwords to Generate: ')
pwdlen = int(plen)
pwdnums = int(pnums)

passwords = pwdgen(pwdlen, pwdnums)

file = open("pass_stor.txt", "a")

for i in range(len(passwords)):
    file.write(passwords[i])

file.close()

print("File closed")