from tkinter import *
from winsound import *

root = Tk()
root.geometry("300x300")

secondTimer = False
minuteTimer = False

def change():
    global timerlabel, timerinput, seconds, minutes, timerseconds
    seconds -= 1
    if timerseconds != 0:
        timerseconds -= 1
    else:
        timerseconds = 59
    if secondTimer == True:
        if len(str(seconds)) == 1:
            timerlabel = Label(root, text="00:0"+str(seconds))
        else:
            timerlabel = Label(root, text="00:"+str(seconds))
        timerlabel.grid(row=4, column=0)
        if seconds != 0:
            timerlabel.after(1000, change)
        if seconds == 0:
            PlaySound("beep-2.wav", SND_FILENAME)
            PlaySound("beep-2.wav", SND_FILENAME)
            PlaySound("beep-2.wav", SND_FILENAME)

def start():
    global timerlabel, timerinput, seconds, minutes, timerseconds
    timerinput = entry.get()
    if timerinput[-1] == "s":
        secondTimer = True
        timerseconds = 0
        seconds = int(timerinput[:-1])
        if len(str(seconds)) == 1:
            timerlabel = Label(root, text="00:0"+str(seconds))
        else:
            timerlabel = Label(root, text="00:"+str(seconds))
        timerlabel.grid(row=4, column=0)
        if seconds != 0:
            timerlabel.after(1000, change)
    if timerinput[-1] == "m":
        minuteTimer = True
        seconds = int(timerinput[:-1])*60
        timerseconds = 0
        minutes = int(timerinput[:-1])
        if len(str(minutes)) == 1:
            timerlabel = Label(root, text="0" + str(minutes) + ":" + str(timerseconds))
        elif len(str(timerseconds)) == 1 and len(str(minutes)) == 1:
            timerlabel = Label(root, text="0" + str(minutes) + ":0" + str(timerseconds))
        elif timerseconds == 0:
            timerlabel = Label(root, text="0" + str(minutes) + ":00" + str(timerseconds))
        elif len(str(timerseconds)) == 1:
            timerlabel = Label(root, text=str(minutes) + ":0" + str(timerseconds))
        else:
            timerlabel = Label(root, text=str(minutes) + ":" + str(timerseconds))
        if seconds != 0:
            timerlabel.after(1000, change)
        timerlabel.grid(row=4, column=0)

entry = Entry(root, width=30)
entry.grid(row=2, column=0, columnspan=20)

button = Button(root, text="Start Timer", command=start)
button.grid(row=3, column=0, columnspan=20)

root.mainloop()
