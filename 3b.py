import random
import string

def randpassword(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters)for i in range(stringLength))


print("generating random password")
choose=str(input("do you want a random password?(y/n)"))
if choose=='y':
     print (" Random password ", randpassword(10) )
elif (choose=='n'):
     print("no password generated")
