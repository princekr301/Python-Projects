

#-----------------------------------------------------------------------------------------------------------------------
# Auther:Prince Kumar
# project Name : Age Caluculator Project
#----------------------------------------------------------------------------------------------------------------------

# The Goal of the Project
#-----------------------------------------------------------------------------------------------------------------------
#Age caluculator program => with the help of this program you can find the age of any person with the help of D.O.B
#-----------------------------------------------------------------------------------------------------------------------


from datetime import date
while True:
	try:
		def agecaluculator(birthday):
			today=date.today()
			age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
			print(f"\nYour Age is :{age}")
		agecaluculator(date(int(input("\nenter date of year :")),int(input("enter date of month :")),int(input("enter birthday :"))))
	except:
		print("enter the date of birth correctly!")
	else:
		print("\nThank you for intrested in Age caluculator!\n ")
	number=input("if you want cheak other person of age then press enter else press  no :")
	if number =="no":
		print("Thank you!\n")
		break

# --------------------------------------------------------------------------------------------------------
# Thanks for watching My Project
#---------------------------------------------------------------------------------------------------------
