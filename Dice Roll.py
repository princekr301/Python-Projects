
#-------------------------------------------------------------
# Auther :- Prince Kumar
# Project Name :- Dice roll generator
#-------------------------------------------------------------
# The goal of this Project playing with your Codding insights and His random Data.🙂🙂


import random
min_value=1
max_value=6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
	x=input("you guess min_value :")
	y=input("you guess max_value :")
	print("dice is rolling....")
	print("the value are :")
	a=random.randint(min_value,max_value)
	b=random.randint(min_value,max_value)
	print(a)
	print(b)
	if x and y == a and b:
		print("you won the game")
	else:
		print("\nyou lost the game\n")
	roll_again=input("Roll Dice again :")