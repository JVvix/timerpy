from tkinter import *
from winsound import *

root = Tk()

secondTimer = False
minuteTimer = False

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

entry = Entry(root, width=30)
entry.grid(row=2, column=0, columnspan=20)

button = Button(root, text="Start Timer", command=start)
button.grid(row=3, column=0, columnspan=20)

root.mainloop()


#  90 
#  90 % 60 = 30
#  90 // 3600 

