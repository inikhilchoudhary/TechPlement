from tkinter import *

import random
import string

def generate_password(length, uppercase=False, lowercase=False, digits=False, special_chars=False):
    characters = []

    if uppercase:
        characters.extend(string.ascii_uppercase)

    if lowercase:
        characters.extend(string.ascii_lowercase)

    if digits:
        characters.extend(string.digits)

    if special_chars:
        characters.extend(string.punctuation)

    if not any([uppercase, lowercase, digits, special_chars]):
        characters = list(string.ascii_letters)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def menu():
    length = int(PassVar.get())  # Get length from Entry widget
    uppercase =Capital.get()   
    lowercase = Small.get()  
    digits = Digit.get()  
    special_chars = Special.get()  

    if length <= 0:
        print("Length must be a positive integer.")
        return

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print("Generated Password:", password)


root = Tk()
root.title("Random Password Generator")
root.geometry("600x200") 

root.minsize(400, 150)
root.maxsize(400, 150)

# Frame for word
WordFrame = Frame(root, borderwidth=5)
WordFrame.grid(row=0, column=0)

#check buttons Buttons for letters num symbol 
Capital=IntVar()
Small=IntVar()
Digit=IntVar()
Special=IntVar()

Checkbutton(WordFrame, text=" A to Z ",variable=Capital).grid(row=0, column=0)
Checkbutton(WordFrame, text=" a to z ",variable=Small).grid(row=1, column=0)
Checkbutton(WordFrame, text=" 0 to 9 ",variable=Digit).grid(row=2, column=0)
Checkbutton(WordFrame, text='''!@#$%^''',variable=Special).grid(row=3, column=0)


# Frame for display result or password
DisplayFrame=Frame(root,bg="Green",borderwidth=5)
DisplayFrame.grid(row=0, column=1)  # Adjusted column

#Label for Password for input
passwordLabel=Label(DisplayFrame,text="Enter Length of Password : ")
passwordLabel.grid(row=0, column=0)  # Adjusted row and column

#input of pass using Entry Widget
PassVar=StringVar()
PassEntry=Entry(DisplayFrame, textvariable=PassVar)
PassEntry.grid(row=0, column=1)  # Adjusted row and column

#Generate Pass Button
Button(DisplayFrame,text="Generate Password",command=menu).grid(row=1, column=0, columnspan=2)  # Adjusted row, column, and columnspan

root.mainloop()
