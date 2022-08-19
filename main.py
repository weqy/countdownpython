import tkinter as tk
import time
import threading
from playsound import playsound
from tkinter import *
from tkinter import messagebox
from tkvideo import tkvideo

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


def play_video():
    canvas1.delete("all")
    player_Label = tk.Label(root)
    canvas1.create_window(200, 100, window=player_Label)
    player = tkvideo("russiankiller.mov", player_Label, loop=1, size=(400, 300))
    player.play()
    time.sleep(1)
    player_Label = tk.Label(root)
    canvas1.create_window(200, 100, window=player_Label)
    player = tkvideo("russianded1.mov", player_Label, loop=1, size=(400, 300))
    player.play()
    threading.Thread(target=playsound, args=('kaboom1.mp3',)).start()
    time.sleep(2)
    player_Label = tk.Label(root)
    canvas1.create_window(200, 100, window=player_Label)
    player = tkvideo("russianded2.mov", player_Label, loop=1, size=(400, 300))
    player.play()
    threading.Thread(target=playsound, args=('kaboom2.mp3',)).start()
    time.sleep(2)
    player_Label = tk.Label(root)
    canvas1.create_window(200, 100, window=player_Label)
    player = tkvideo("russianded3.mov", player_Label, loop=1, size=(400, 300))
    player.play()
    threading.Thread(target=playsound, args=('kaboom3.mp3',)).start()


# declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Using Entry class to take input from the user
hour_box = tk.Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=hour
)

canvas1.create_window(150, 140, window=hour_box)


mins_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=minute)

canvas1.create_window(195, 140, window=mins_box)

sec_box = Entry(
    root,
    width=3,
    font=("Arial", 18, ""),
    textvariable=second)

canvas1.create_window(240, 140, window=sec_box)

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
            play_video()

        # decresing the value of temp
        # after every one sec by one
        user_input -= 1


button1 = tk.Button(text='Enter', command=threading.Thread(target=countdowntimer).start)
canvas1.create_window(200, 200, window=button1)

root.mainloop()
