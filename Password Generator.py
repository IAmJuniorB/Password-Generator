
from tkinter import *

# use to copy our generated pw to clipboard
import pyperclip

# for generating random pw
import random

# initializing tkinter
root = Tk()

photo = PhotoImage(file='Junior.jpg')

root.title('PW Gen - Joe')

# setting the width and height of the gui
root.geometry("500x250")    # x small case here

# declaring variable of str type. Variable will be used to store pw generated
passstr = StringVar()

# declaring variable of int type which will be used to store length of pw entered by user
passlen = IntVar()

# setting the length of pw to zero
passlen.set(0)


# function to generate pw
def generate():
    # storing keys in a list which will be used to generate pw 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')', '-', '_', '=', '+', '"', "'", ':',
            ';', '>', '<', '?', '/', '\\', '|', '[', ']', '.']

    # declaring empty string
    password = ""

    # loop to generate random password of the length entered by the user
    for _ in range(passlen.get()):
        password += random.choice(pass1)

    # setting password to entry widget
    passstr.set(password)

# function to copy password to clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating text label widget
Label(root, text="Password Generator", font="calibri 25 bold").pack()

# Creating text label widget
Label(root, text="Enter password length").pack(pady=3)

# Creating widget to take pw length entered by user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# Creating text label widget
Label(root, text="Password Generated").pack(pady=3)

# entry widget to show generated pw
Entry(root, textvariable=passstr).pack(pady=3)

# button to call copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

# mainloop() - infinite loop to run application when in ready state 
root.mainloop()

"""
Feel free to commment/critique anything here
Would also love to gain some understanding as to why PhotoImage() does not work for me
Thanks
"""