from tkinter import *
root=Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.minsize(400,300)

BgPic=PhotoImage(file="Bg.png")
BgPicLabel=Label(image=BgPic)
BgPicLabel.pack()

root.mainloop()