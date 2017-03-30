import tkinter
from tkinter import *
def lopeta():
 import sys
 root.destoy()
 sys.exit(0)
root = tkinter.Tk()
root.title("Esimerkkiohjelma")
frame = Frame(root)
frame.pack()
kanvas = Canvas(frame, width = 800, height = 600)
kuva = PhotoImage(file = "kuva")
kanvas.create_image(800,600,image = kuva)
kanvas.pack(side = TOP)
button = Button(frame, text="QUIT", command=lopeta)
button.pack(side=BOTTOM)
root.mainloop()
