

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Auther : Prince Kumar sharma
# Project Name : Create Account and Log in Account.
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

#user id nad password create a new account and log in 
#-----------------------------------------------------------------------------------
print("Create a new account")
a=input("Enter you name :-")
b=input("Mother's name :-")
c=input("D.O.B  :-")

y=input("enter user id  :")
p=input("enter password :")
r=input("enter password again :")
print("\nThank you accoount created sucsesfuly!\n welcome to this app!")
print("\nLog in your acount now\n")
user=input("enter your user id :")
if user==y:
	d=input("enter again user id :")
	if d==y:
		m=input("enter password !")
		if m==p:
			print("thankyou")
			print("Your account created sucsesfuly")
		else:
			e=input("enter password again :")
			if e==p:
				print("welcome to prince home!")
			else:
				print("Try again after sometime!")
else:
	print("wrong user id ")
	f=input("enter user id again :")
	if f==y:
		g=input("password :")
		if g==p:
			print("You are sucsesfuly logged in !")
	else:
		print("try diffrent password!")


# ---------------------------------------------------------------
# Thanks For Watching My Python Project .....
# ---------------------------------------------------------------