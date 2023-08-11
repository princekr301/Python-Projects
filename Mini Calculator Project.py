
#--------------------------------------------------------------------------
#  Auther :- Prince kumar sharma
#  Project Name :- Mini Calculator
#--------------------------------------------------------------------------
#		Mini caluculator 
#		this project coluculate any two number. and any operators
#--------------------------------------------------------------------------

try:
# mini caluculator program
	first=input("enter first number :")
	operator=input("enter operator(+ - * / ** % // ) : ")
	second=input("enter second number :")
	first=float(first)
	second=float(second)

	if operator=="+":
		output=(first+second)
	elif operator=="-":
		output=(first-second)
	elif operator=="*":
		output=(first*second)
	elif operator=="/":
		output=(first/second)
	elif operator=="%":
		output=(first%second)
	elif operator=="//":
		output=(first//second)
	elif operator=="**":
		output=(first**second)
	#else:
	#	output=("invalid number")
	print(f"Output :{output}")
except:
	print("please enter number correctly!")
	print("please enter operator correctly!")
else:
	print("Caluculate Again!")
finally:
	print("!")



#--------------------- (OR) -------------------------------
# If You are Lazy(🤪) or if you don't want to write extra Code than 
# You can try this for Mini Caluculator.😅😅😅

# It also Work same like above Project

x=eval(input("enter num operator 2nd :-"))
print(x)


# Thank You for watching My Project
# please give Your Review How is that.