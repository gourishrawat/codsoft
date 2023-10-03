import random
from tkinter import * 

root = Tk()
root.title('Random Password Generator ')
root.geometry('850x850')

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_'

characters = alpha + numbers + symbols

label_characters = Label(root, text="Enter the Number of characters Below", bg='gray',font=('Arial', 22)).pack(padx=10)
character_length = Entry(root,font="Arial 22")
character_length.pack(padx=10)

def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text='Generated Password: ' + password ,font=('Arial', 22))

Button(root, text="Generate Password", command=generate_password,bg='azure', font=('Arial', 20)).pack(padx=10)
label_password = Label(root,bg='brown2', font=('Arial', 12))
label_password.pack()

label_characters = Label(root, text="THANK YOU FOR USEING THIS PASSWORD GENERATOR",font=('Arial', 22)).pack(padx=10)

root.mainloop()