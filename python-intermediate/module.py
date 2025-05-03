import os
os.getcwd()
work_dir = os.getcwd()
print(work_dir)

#change directory
os.chdir("C:\python")
os.getcwd()
print(work_dir)

#get local environment
print(os.environ)

from os import chdir , getcwd

print(getcwd())

import string

#print all ascii lowercase characters
print(string.ascii_lowercase)

#print punctuation
print(string.punctuation)


from datetime import date
deadline = date(2024, 1, 19)
print(type(deadline))
print(deadline)
