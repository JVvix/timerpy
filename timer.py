import time
from playsound import playsound

def countdown(total_time):
    total_time = int(total_time)
    two_digit_seconds = 59
    str_two_digit_seconds = str(two_digit_seconds)
    str_minutes = str(minutes)
    seconds = int(minutes * 60)
    while(seconds != 0):
        if int(str_two_digit_seconds) == 00:
            if seconds > 59:
                minutes -= 1
                two_digit_seconds = 59
                str_two_digit_seconds = "59"
            seconds -= 1
            two_digit_seconds -= 1
            str_two_digit_seconds = str(two_digit_seconds)
            print(str_minutes + ": " + two_digit_seconds)
    playsound("beep-2.wav")
    playsound("beep-2.wav")
    playsound("beep-2.wav")

input_time = input("how much time do you plan to time for? ")
if input_time[-1] == "h":
    seconds = int(time[:-1]) * 3600
    #hours = time[:-1]
if input_time[-1] == "m":
    #minutes = time[:-1]
    seconds = int(input_time[:-1]) * 60
    
print('hour: ' + input_time[:-1])
print('seconds: ' + str(seconds))

while(seconds > 0):
    #time.sleep(1)
    #print(seconds)
    display_minutes = seconds // 60
    display_seconds = seconds % 60
    if int(display_seconds) < 10:
        display_seconds = "0" + str(display_seconds)
    print(str(display_minutes) + ':' + str(display_seconds))
    time.sleep(1)
    seconds = seconds - 1

playsound("beep-2.wav")
playsound("beep-2.wav")
playsound("beep-2.wav")
#for i in range(len(time)):



#countdown(time)
