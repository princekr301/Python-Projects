# ------------------------------------------------------------------------------------------
#  Auther: Prince Kumar Sharma
#  Project Name: State and Capital Project
#-------------------------------------------------------------------------------------------

# The Goal of the Project is Input the State and Output show the capital of the State.
# ------------------------------------------------------------------------------------------
while True:
	try:
	# Make a program so that when enter a state by user ,
	# its capital will be shown
		state_capital={
		"bihar": 	"patna",
		"assam":  		"dispur",
		"uttar pradesh":	 "lucknow",
		"rajsthan": 			 "jaipur",
		"goa": 						"panji",
		"kerala":						"Thiruvananthapuram",
		"manipur": 							"imphal",
		"gujarat": 								"gandhinagar",
		"jharkhand":						 		"ranchi",
		"madhya pradesh":						 		"bhopal",
		"punjab": 											"chandigarh",
		"tamil nadu":										 "chennai",
		"west bengal":											 "kolkata",
		"uttarakhand":												 "dehradun",
		"odisha":														"bhubaneswar",
		"Arunachal pradesh":										 "itanagar",
		"chhatisgarh": 												"raipur",
		"haryana": 												"chcandigarh",
		"himachal pradesh":									 "shimla",
		"karnatka": 										"bengaluru",
		"meghalaya": 									"shillong",
		"mizoram": 									"aizawl",
		"nagaland":								 "kohima",
		"sikkim":							 "gangtok",
		"telangana": 						"Hyderabad",
		"tripura": 						"Agartala",
		"channai" :					"Tamilnadu",
		"maharstra":			"Mumbai",
		"jammu and kashmir" :"Srinagar"
		}
#-------------------------------------------------------------------------------------------------------
		x=input("\nenter the name of state :-")
		print("the capital of",x,"is",state_capital[x])
	except:
		print("\nplease enter the state name correctly :")
	else:
		print("that's great!")
	#finally:
		#print("good luck")
	x=input("\nif you wnat to break this program then press b  else press enter :")
	if x=="b":
		print("thank you!")
		break

# --------------------------------------------------------------------------------------------------------
# Thanks for watching My Project
#---------------------------------------------------------------------------------------------------------

# ---------------------------------------(OR)----------------------------------------------

while True:
	try:
		state_capital={
		"Andhra Pradesh":	"Amaravati",
		"Arunachal Pradesh":"Itanagar",
		"Assam":"Dispur",
		"Bihar":"Patna",
		"Chhattisgarh":	"Naya Raipur",
		"Goa":	"Panaji",
		"Gujarat":	"Gandhinagar",
		"Haryana":	"Chandigarh",
		"Himachal Pradesh":	"Shimla",
		"Jharkhand":	"Ranchi",
		"Karnataka":"Bengaluru (formerly Bangalore)",
		"Kerala":	"Thiruvananthapuram",
		"Madhya Pradesh":	"Bhopal",
		"Maharashtra":	"Mumbai",
		"Manipur":	"Imphal",
		"Meghalaya":	"Shillong",
		"Mizoram":	"Aizawl",
		"Nagaland":	"Kohima",
		"Odisha":	"Bhubaneswar",
		"Punjab":	"Chandigarh",
		"Rajasthan":	"Jaipur",
		"Sikkim":	"Gangtok",
		"Tamil Nadu":	"Chennai",
		"Telangana":	"Hyderabad",
		"Tripura":	"Agartala",
		"Uttar Pradesh":"Lucknow",
		"Uttarakhand":	"Dehradun, Gairsain (Summer)",
		"West Bengal":	"Kolkata"}
		y=input("\nenter the name of state :")
		yy=state_capital[y]
		print(f"The capital of {y} is :{yy}!")

	except:
		print("please enter First letter in capital letter of state :")
	else:
		print("That's Great!\n")
	x=input("if you want to break this program then press  p  else press enter :")
	if x=="p":
		print("Thanks for you suport!")
		break
