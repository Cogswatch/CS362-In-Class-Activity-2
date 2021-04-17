# Inspired by https://www.pythonforbeginners.com/code-snippets-source-code/script-password-generator
import string

from random import *
charset = string.ascii_letters + string.digits

def password(n):
  print("Password of length ", n, ": ")
  # See link above for source
  password =  "".join(choice(charset) for x in range(randint(8, 16)))
  print(password)

password(18)