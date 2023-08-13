
#-----------------------------------------------------------------------------------------------
# Auther:Prince Kumar
# project Name : Snake Water Run Game
#-----------------------------------------------------------------------------------------------

# The Goal of the Project
#-----------------------------------------------------------------------------------------------
#snake water and gun game
#-----------------------------------------------------------------------------------------------

import random
while True:
	try:

		def game(comp,you):
			if comp==you:
				return None
			if comp=="s":
				if you=="w":
					return False
				elif you=="g":
					return True
			elif comp=="w":
				if you=="g":
					return False
				elif you=="s":
					return True
			elif comp=="g":
				if you=="s":
					return False
				elif you=="w":
					return True

		print("computer choose sanke (s) gun (g)  water (w) :-")
		co = random.randint(1,3)
		if co==1:
			comp="s"
		elif co==2:
			comp="g"
		elif co==3:
			comp="w"
		you=input("Your choice :sanke (s) gun (g)  water (w) :- ")
		a=game(comp,you)

		print("You choice :",you)
		print("comp choice :",comp)

		if a==None:
			print("The game is tie !")
		elif a==True:
			print("You won the game !")
		else:
			print("You lose the game !")
	except:
		print("enter name correctly!")
	else:
		print("good job!")
	a=input("if you want to break the game press y")
	if a=="y":
		print("thanks")
		break

# --------------------------------------------------------------------------------------------------------
# Thanks for watching My Project
#---------------------------------------------------------------------------------------------------------
