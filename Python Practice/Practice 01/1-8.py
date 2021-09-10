# Get the user input for current time, waiting time, and zone
currentTime = float (input("Enter the current time in hours "))
waitHour = float(input("Enter the waiting time in hours "))
timeLine= input("Enter AM or PM ")
         
#Figure out whether the new hour after the waiting time is in pm or am         
if (timeLine == "AM"):
    currentTimeLine = timeLine
    otherTimeLine = "PM"             
else:
    currentTimeLine = "PM"
    otherTimeLine ="AM"
    
         
sum = currentTime + waitHour
                 
                 
#narrow down the sum to 24 hours so that anything less than 
zone = sum%24

if(zone <=12):
    newTimeLine = currentTimeLine
else:
    newTimeLine = otherTimeLine

clockTime = zone%12
print(f'The clock hour after waiting time is {clockTime} {newTimeLine}')
                 

    