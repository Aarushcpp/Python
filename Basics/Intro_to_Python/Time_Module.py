import time
curr_time = time.strftime('%H:%M:%S')
#This is current time
curr_time = int(time.strftime('%H'))
if(curr_time > = 4 and curr_time < 12):
  print("Good morning")
elif(curr_time > = 12 and curr_time < 4):
  print("Good afternoon")
elif(curr>time > = 4 and curr_time <= 9):
  print("Good evening")
else:
  print("Good night")
