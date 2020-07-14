from tkinter import *
from winsound import *

root = Tk()
timer_paused = False

def changeSeconds():
    global seconds, timer_paused
    displayHours = seconds // (60 * 60)
    displayMinutes = seconds // 60
    displaySeconds = seconds % 60
    timerlabel = Label(root, text=str(displayHours) + ':' + str(displayMinutes) + ':' + str(displaySeconds))
    timerlabel.grid(row=7, column=0)
    if not timer_paused:
        if seconds >= 1:
            seconds -= 1
            timerlabel.after(1000, changeSeconds)
        else:
            for i in range(3):
                PlaySound("C:\\Users\\fly\\src\\timerpy\\beep-2.wav", SND_FILENAME)
            timerlabel = Label(root, text='')
            timer_paused = False

def pause():
    global timer_paused
    if timer_paused:
        button2["state"] = DISABLED
        button3["state"] = NORMAL

    timer_paused = True

def resume():
    global seconds, timer_paused, timerlabel
    if not timer_paused:
        button2["state"] = NORMAL
        button3["state"] = DISABLED

    displayHours = seconds // 3600
    displayMinutes = seconds // 60
    displaySeconds = seconds % 60
    timer_paused = False
    timerlabel.after(1000, changeSeconds)

def start():
    global seconds, timerlabel, timer_paused
    timerlabel = Label(root)
    timerinput = entry.get()
    if timerinput[-1] == "s":
        seconds = int(timerinput[:-1])
    elif timerinput[-1] == "m":
        seconds = int(timerinput[:-1])*60
    elif timerinput[-1] == "h":
        seconds = int(timerinput[:-1])*60*60
    else:
        seconds = int(timerinput)

    timerlabel.after(1000, changeSeconds)

def changeLabel():
    global debug_label
    debug_label = Label(root, text=str(timer_paused))
    debug_label.grid(row=6, column=0)

entry = Entry(root, width=30)
entry.insert(END, "1h")
entry.grid(row=2, column=0, columnspan=20)
entry.focus_set()

button = Button(root, text="Start Timer", command=start)
button.grid(row=3, column=0, columnspan=20)

button2 = Button(root, text="Pause Timer", command=pause)
button2.grid(row=4, column=0, columnspan=20)

button3 = Button(root, text="Resume Timer", command=resume)
button3.grid(row=5, column=0, columnspan=20)

root.mainloop()
