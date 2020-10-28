
import datetime

now = datetime.datetime.now()

current_time = now.strftime("%H:%M:%S")
current_hour = now.hour
current_minute = now.minute
current_second = now.second
print("Current time is: " + str(current_time))

def past(current_hour, current_minute, current_second):
    milliseconds = int((current_hour*60*60*1000) + (current_minute*60*1000) + (current_second*1000))
    return milliseconds

print("This equals " + str(past(current_hour, current_minute, current_second)) + " milliseconds")