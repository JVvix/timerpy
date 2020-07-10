from tkinter import *
from winsound import *

root = Tk()

secondTimer = False
minuteTimer = False

def changeMinutes():
    global timerlabel, timerinput, seconds, minutes, timerseconds
    secondsLabel = Label(root, text=str(seconds))
    secondsLabel.grid(row=6, column=0)
    secondsLabel2 = Label(root, text=str(timerseconds))
    secondsLabel2.grid(row=7, column=0)
    seconds -= 1
    if seconds == 0:
        timerlabel.config(text="00:00")
    if timerseconds != 0:
        timerseconds -= 1
    else:
        timerseconds = 59
        minutes -= 1
    secondsLabel = Label(root, text=str(seconds))
    secondsLabel.grid(row=6, column=0)
    timerlabel.grid(row=4, column=0)
    if len(str(minutes)) == 1:
        timerlabel = Label(root, text="0" + str(minutes) + ":" + str(timerseconds))
    elif len(str(timerseconds)) == 1 and len(str(minutes)) == 1:
        timerlabel = Label(root, text="0" + str(minutes) + ":0" + str(timerseconds))
    elif timerseconds == 0:
        timerlabel = Label(root, text="0" + str(minutes) + ":0" + str(timerseconds))
    elif len(str(timerseconds)) == 1:
        timerlabel = Label(root, text=str(minutes) + ":0" + str(timerseconds))
    else:
        timerlabel = Label(root, text=str(minutes) + ":" + str(timerseconds))
    if seconds != 0:
        timerlabel.after(1000, changeMinutes)
    if seconds == 0:
        timerlabel.config(text="00:00")
        PlaySound("beep-2.wav", SND_FILENAME)
        PlaySound("beep-2.wav", SND_FILENAME)
        PlaySound("beep-2.wav", SND_FILENAME)

def changeSeconds():
    global seconds
    displayHours = seconds // 3600
    displayMinutes = seconds // 60
    displaySeconds = seconds % 60
    timerlabel = Label(root, text=str(displayHours) + ':' + str(displayMinutes) + ':' + str(displaySeconds))
    timerlabel.grid(row=4, column=0)
    if seconds >= 0:
        seconds -= 1
        timerlabel.after(1000, changeSeconds)
    else:
        for i in range(2):
            PlaySound("beep-2.wav", SND_FILENAME)
            timerlabel = Label(root, text=str(displayHours) + ':' + str(displayMinutes) + ':' + str(displaySeconds))

def start():
    global seconds
    global timerlabel 
    timerlabel = Label(root)
    timerinput = entry.get()
    if timerinput[-1] == "s":
        seconds = int(timerinput[:-1])
    if timerinput[-1] == "m":
        seconds = int(timerinput[:-1])*60
    if timerinput[-1] == "h":
        seconds = int(timerinput[:-1])*60*60

    timerlabel.after(1000, changeSeconds)

def start2():
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
            timerlabel.after(1000, changeSeconds)
    if timerinput[-1] == "m":
        minuteTimer = True
        seconds = int(timerinput[:-1])*60+1
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
            timerlabel.after(1000, changeMinutes)
        timerlabel.grid(row=4, column=0)

entry = Entry(root, width=30)
entry.grid(row=2, column=0, columnspan=20)

button = Button(root, text="Start Timer", command=start)
button.grid(row=3, column=0, columnspan=20)

root.mainloop()


#  90 
#  90 % 60 = 30
#  90 // 3600 

