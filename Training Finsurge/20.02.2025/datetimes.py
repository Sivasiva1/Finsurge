
from datetime import datetime
#current date 
now = datetime.now()

#Extract Date & Time Components
print("date ",now)
print("year ",now.year)
print("month ",now.month)
print("day ",now.day) 
print("Hour ",now.hour)
print("Minute ",now.minute)
print("Sec ",now.second) 

#create a specific datetime 
newdatetime = datetime(2025,2,20,16,4,59) 
print(newdatetime) 

#strftime 
newdatetime= now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date & Time:", newdatetime)

from datetime import timedelta 

print(now + timedelta(days=10))

print(now - timedelta(days=10))

#print(now+ timedelta(month=10))  error 


print(now + timedelta(hours=10))

print(now - timedelta(hours=10))

date1 = datetime(20,2,11)
date2 = datetime(2025,1,11)
#date2 = datetime(2025,1,111)
print(date1-date2) 

#string to datetime conversion 

string = "2025-02-20"
date = datetime.strptime(string, "%Y-%m-%d")

print("Converted Date:", date)



string = "20250-02-20 10:00:00"
date = datetime.strptime(string, "%Y-%m-%d %H:%M:%S") 

print("Converted Date:", date) 

