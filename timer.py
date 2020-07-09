from tkinter import *

root = Tk()
root.geometry("300x300")

def change():
    global timerlabel, timerinput, seconds

    seconds -= 1
    timerlabel.config(text=str(seconds))
    timerlabel.grid(row=4, column=0)
    if seconds != 0:
        timerlabel.after(1000, change)

def start():
    global timerlabel, timerinput, seconds
    timerinput = entry.get()
    if timerinput[-1] == "s":
        seconds = int(timerinput[:-1])
        timerlabel = Label(root, text=str(seconds))
        timerlabel.grid(row=4, column=0)
        if seconds != 0:
            timerlabel.after(1000, change)

entry = Entry(root, width=30)
entry.grid(row=2, column=0, columnspan=20)

button = Button(root, text="Start Timer", command=start)
button.grid(row=3, column=0, columnspan=20)

root.mainloop()
