from tkinter import *
import pyperclip
from random import choice
from string import printable

root = Tk()

photo = PhotoImage(file='Junior.png')
root.iconphoto(False, photo)

root.title('PW Gen - Joe')

root.geometry("500x250")

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate_password() -> str:
    random_characters = list(printable)[:-5]
    password = ""
    for _ in range(passlen.get()):
        password += choice(random_characters)
    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator", font="calibri 25 bold").pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=passlen).pack(pady=3)

Button(root, text="Generate Password", command=generate_password).pack(pady=7)

Label(root, text="Password Generated").pack(pady=3)

Entry(root, textvariable=passstr).pack(pady=3)

Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

root.mainloop()

"""
Feel free to commment/critique anything here
Would also love to gain some understanding as to why PhotoImage() does not work for me
Thanks
"""
