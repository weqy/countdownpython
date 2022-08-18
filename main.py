import tkinter as tk
from tkinter import *
import random
import string
from tkvideo import tkvideo


root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=600, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate the Square Root')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='How many characters would you like?')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

var1 = IntVar()
scale1 = tk.Scale(root, from_=5, to=15, orient=HORIZONTAL, variable=var1, showvalue=bool(0))
canvas1.create_window(200, 140, window=scale1)  # shows entry in canvas
scale_val_label = tk.Label(root, textvariable=var1)
canvas1.create_window(250, 140, window=scale_val_label)

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    user_input = int(scale1.get())
    random.shuffle(characters)
    password = []
    for x in range(user_input):
        password.append(random.choice(characters))

    random.shuffle(password)
    my_result = ("".join(password))
    label2 = tk.Label(root, text='Your password is: ' + my_result)
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 220, window=label2)


button1 = tk.Button(text='Generate Password', command=generate_password, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
