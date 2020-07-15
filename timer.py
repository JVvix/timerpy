from pid import PidFile
from tkinter import *
from winsound import *

root = Tk()

run = True
timer_paused = False
old_timer_paused = timer_paused

def check():
    if pause_button["state"] == "active":
        pause_button["state"] = "disabled"
        resume_button["state"] = "normal"

    if resume_button["state"] == "active":
        pause_button["state"] = "normal"
        resume_button["state"] = "disabled"
    
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
    old_timer_paused = timer_paused
    timer_paused = True
    pause_button["state"] = "disabled"
    resume_button["state"] = "normal"

def resume():
    global seconds, timer_paused, timerlabel

    pause_button["state"] = "normal"
    resume_button["state"] = "disabled"

    displayHours = seconds // 3600
    displayMinutes = seconds // 60
    displaySeconds = seconds % 60
    old_timer_paused = timer_paused
    timer_paused = False
    timerlabel.after(1000, changeSeconds)

def start():
    global seconds, timerlabel, timer_paused
    pause_button["state"] = "normal"
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

start_button = Button(root, text="Start Timer", command=start)
start_button.grid(row=3, column=0, columnspan=20)

pause_button = Button(root, text="Pause Timer", command=pause)
pause_button.grid(row=4, column=0, columnspan=20)

resume_button = Button(root, text="Resume Timer", command=resume)
resume_button.grid(row=5, column=0, columnspan=20)

pause_button["state"] = "disabled"
resume_button["state"] = "disabled"

# root.after(1, check)
root.mainloop()
