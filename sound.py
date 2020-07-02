from playsound import playsound
import time

seconds = 6

for i in range(seconds):
    print(seconds)
    time.sleep(1)
    seconds -= 1

playsound("beep-2.wav")
