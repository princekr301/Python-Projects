
# ------------------------------------------------------
# Auther : Prince Kumar sahrma
# Project Name :  Random Password Generator
# ------------------------------------------------------

#random password generator


import random

x="abcdefghijklmnopqrstuvwxyz"
y="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
z="!@#$%^&*/"
a="1234567890"
mix=x+y+z+a
lenth=8

password="".join(random.sample(mix,lenth))
#password=random.randint(mix,lenth)
print(f"Your new password is :=> {password}")


# ----------------------------------------------------------
# Thanks For Watching My  Python Project
# ----------------------------------------------------------
