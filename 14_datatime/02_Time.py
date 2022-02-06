from datetime import time
import datetime

time_1 = time()
print(time_1) # 00:00:00


time_2 = time(16,13,12)
print(time_2) # 16:13:12


print("Hour:",time_2.hour)
print("Minute:",time_2.minute)
print("Second:",time_2.second)



# Formatting

now = datetime.datetime.now()
my_time = now.strftime("%H:%M:%S") 
print(my_time) #16:17:49