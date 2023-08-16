
# ---------------------------------------------------------------------------------
# Auther : Prince Kumar sharma
# Project Name : Alarm Project
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
#countdown project or alarm setup
# ---------------------------------------------------------------------------------


from datetime import datetime
import winsound
#from playsound import playsound
alarm_time=input("enter the time of alarm to be set :HH:MM:SS \n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:]
#alarm_period=alarm_time[9:11].upper()
print("setting up alarm")
print(alarm_hour)
print(alarm_minute)
print(alarm_second)
#print(alarm_period)
while True:
	now=datetime.now()
	current_hour=now.strftime("%I")
	current_minute=now.strftime("%M")
	current_second=now.strftime("%S")
	#current_period=now.strftime("%p")
	#if (alarm_period==current_period):
	if (alarm_hour==current_hour):
		if (alarm_minute==current_minute):
			if (alarm_second==current_second):
				print(" Its time to wake up !")
				break
# ------------------------------------------------------------------
# Thanks For Watching My Project
# -----------------------------------------------------------------