
#- -------------------------------------------------------------------------------------------------------
# Auther : Prince Kunmar sharma
# Project Name : ATM Project
#---------------------------------------------------------------------------------------------------------

#ATM machine project
#---------------------------------------------------------------------------------------------------------

import time
print("=========================.......---------------.............................................................................")
print("Welcome to Prince Bank !!")
time.sleep(4)
print("----------------------------------------------------------------------------------------------------------------------------")
print("please insert your card!")
time.sleep(5)
password=1234
balance=14500
chance=4
#print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("**************************************************************************************************************")
print("""choice your option
	1==balance inquairy
	2==withdrawl_balance
	3==credit balance
	4==exit
---------------------------------------------------------------------------------------------------------------------------------""")
time.sleep(2)
option=int(input("selcet option :"))

while True:
	if option==1:
		time.sleep(3)
		while chance!=0:
			print("---------------------------------------------------------------------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("------------------------------------------------------------------------------------------------------------")
			else:
			# password==pin:
				print("-----------------------------------------------------------------------------------------------------------")
				#print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---\n")
				print("please wait cheaking your account!")
				time.sleep(3)
				print(f"Your balnce is {balance}")
				time.sleep(3)
				print("\nthank you for Using Prince Bank !!")
				break
		
	elif option==2:
		withdrawl_amount=int(input("enter your ammount:"))
		time.sleep(3)
		while chance!=0:
			print("-----------------------------------------------------------------------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("-----------------------------------------------------------------------------------------------------------")
			else:

			# password==pin:
				print("----------------------------------------------------------------------------------------------------------")
		
				print("please wait transaction is being processing!")
				time.sleep(4)
				print("please collect your ammount!")
				time.sleep(2)
				balance=balance-withdrawl_amount
				print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
				print(f"Your left balance is {balance}")
				time.sleep(3)
				print("\nThank you for Using Prince Bank !!")
				break

	elif option==3:
		credit=int(input("Enter your credit amount :"))
		time.sleep(2)
		while chance!=0:

			print("---------------------------------------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("-------------------------------------------------------------------------------")
			else:

			# password==pin:
				print("--------------------------------------------------------------------------------")
		
				print("Put your ammount in the ATM ! slot")
				time.sleep(2)
				print("please wait your amount is adding !")
				time.sleep(3)
				balance=balance+credit
				print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--__---_-----____------___")
				print(f"Your updated amount is {balance}")
				time.sleep(2)
				print("\nThank you for using Prince Bank !!")
				break
	elif option==4:
		print("Thank you for your support")
	user_exit=input("\nWould you like to use again?  press Yes/No  :")
	if user_exit=="Yes":
		print("\n///////////////////////////////////////////////////////////////////")
		print("\nThank you for using Prince bank !!")
		continue
	else:
		break



# ------------------------------------------------------------------------------------------------
# Thanks For Watching My Qute  Automatic Trainer Machine(ATM) Project.
# ------------------------------------------------------------------------------------------------