#--------------------------------------------------------------------------
# Auther :-  Prince Kumar Sharma
# Project NAme :- Result Declearation Project
#--------------------------------------------------------------------------
#	In this project i can check the reult of all student by the input of 
#	name.
#	you will display the full marks, obtained marks,persantage,and
#	student greeting for this work.



cheak="y"
while cheak=="y":
	try:
		print("ıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı")
		result={
		"prince kumar":{"hnd":98,"math":90,"eng":86,"sc":94,"sst":82},
		"ankit kumar": {"hnd":88,"math":60,"eng":96,"sc":94,"sst":92},
		"manu singh":  {"hnd":79,"math":81,"eng":66,"sc":64,"sst":78},
		"kumod kumar": {"hnd":89,"math":91,"eng":56,"sc":54,"sst":68},
		"anmol asha":  {"hnd":70,"math":85,"eng":63,"sc":54,"sst":70},
		"priya sharma":{"hnd":40,"math":55,"eng":53,"sc":54,"sst":68},
		"chhotu kumar":{"hnd":20,"math":35,"eng":53,"sc":24,"sst":18},
		"priyanshu kumar":{"hnd":30,"math":35,"eng":35,"sc":46,"sst":59}
		}
		#if you want to update the marks of student then use this method
		#result["prince kumar"]["hnd"]=30
		#result["Ankit kumar"].update({"hnd":50})
		#result.pop("chhotu kumar") # to delete the marksheet


		name=input("Name of student:")
		ob_marks=sum(result[name].values())
		per=(sum(result[name].values())/500)*100
		per=ob_marks/5	
	#print(result["prince"].values())
		print(f"Full marks     : 500")
		print("Obtained marks :",ob_marks)
		print(f"percentage     :{per}%")
		if ob_marks>300:
			div="First Divison"
		elif ob_marks>225:
			div="Second Divison"
		elif ob_marks>200:
			div="Third Divison"
		else:
			div="Fail"
		print(f"Divison        : {div}")
	except:
		print("please enter student name correctly !")
		print("There is no student by this name!")
	else:
		print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")
	finally:
		print("★彡[ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ★ᴘʀɪɴᴄᴇ ᴋᴜᴍᴀʀ★]彡★")
	cheak=input("If you want to cheak another student of result then press y  else n :")







#------------------------------------------------------------------
# In this Project we can check the Result based on his Roll Number
#------------------------------------------------------------------


try:
	print("\nıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı,⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı\n")
	x={1:{"hnd":64,"eng":56,"math":89,"sc":64,"sst":63},
	2:{"hnd":65,"eng":59,"math":59,"sc":55,"sst":78},
	3:{"hnd":58,"eng":72,"math":80,"sc":40,"sst":36},
	4:{"hnd":33,"eng":66,"math":66,"sc":78,"sst":47},
	5:{"hnd":64,"eng":36,"math":44,"sc":64,"sst":90},
	6:{"hnd":33,"eng":86,"math":70,"sc":30,"sst":44}}
	#print(x)
	y=int(input("Roll Number   :- "))
	mark_ob=sum(x[y].values())
	per=mark_ob/500*100
	if y==1:
		print("\nStudent Name  :- Prince kumar")
	elif y==2:
		print("\nStudent Name  :- Kumod kumar")
	elif y==3:
		print("\nStudent Name  :- Ankit kumar")
	elif y==4:
		print("\nStudent Name  :- Rahul kumar")
	elif y==5:
		print("\nStudent Name  :- Manu singh")
	elif y==6:
		print("\nStudent Name  :- Anmol asha")
	else:
		print("Not Record found")

	print(f"Obtained Marks :- {mark_ob}")
	print(f"Persantage     :- {per}")
	if mark_ob>=300:
		print("Divison  :- First divison")
	elif mark_ob>=225:
		print("Divison 	:- Second divison")
	elif mark_ob>=200:
		print("Divison  :- Third divison")
	else:
		print("fail")
except:
	print("Result not found!")
	print("Please enter correct roll number!")
else:
	print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")


	