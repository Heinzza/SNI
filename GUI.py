import tkinter
from tkinter import *
def lopeta():
    import sys
    pohja.destroy()
    sys.exit(0)
pohja = tkinter.Tk()
pohja.title("Senior Notification Interface")
label = tkinter.Label(pohja,text="HEI, MITÄ KUULUU?")
label.pack()
button = tkinter.Button(pohja, text = "QUIT", command=lopeta)
button.pack(side = BOTTOM)

pohja.mainloop()

