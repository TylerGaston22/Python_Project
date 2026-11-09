# 23 - Countdown timer
# Count down from a number of seconds, showing the time as HH:MM:SS.
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")   # 0 is padding, 2 is digits
    time.sleep(1)

print("Time's up!")
