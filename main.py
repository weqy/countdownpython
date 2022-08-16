# Desktop Notifier
# V.1.3 11:44AM 8/1/22

import tkinter as tk
from plyer import notification
import time
import threading
from playsound import playsound
from tkinter import *
from tkinter import messagebox


root = tk.Tk()

root.title("countdown")

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

label1 = tk.Label(root, text='Countdown')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="How long do you want to wait until your notification?")
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)



# declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Using Entry class to take input from the user
hour_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=hour
)

hour_box.place(x=130, y=140)

mins_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=minute)

mins_box.place(x=175, y=140)

sec_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=second)

sec_box.place(x=220, y=140)


def countdowntimer():
    try:
        # store the user input
        user_input = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning('INVALID', 'Invalid Input!')
    while user_input > -1:

        mins, secs = divmod(user_input, 60)

        # Converting the input entered in mins or secs to hours,
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        # store the value up to two decimal places
        # using the format() method
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window
        root.update() # updates GUI 
        time.sleep(1) # every 1 second


        if (user_input == 10): # 10 seconds left until countdown end
            playsound('tensecleft.mp3') # plays sound

        # if user_input value = 0, then a messagebox pop's up
        # with a message
        if (user_input == 0): # countdown end
            #messagebox.showinfo("Time Countdown", "Time Over")
            threading.Thread(target=playsound, args=('timeup.mp3',)).start() # makes timeup.mp3 part of messagebox notif
            messagebox.showinfo("Time's up!", 'Timer went off!') # popup notif


        # decresing the value of temp
        # after every one sec by one
        user_input -= 1

button1 = tk.Button(text='Enter', command=threading.Thread(target=countdowntimer).start)
canvas1.create_window(200, 200, window=button1)

root.mainloop()
