import tkinter
from tkinter import *

def lopeta():
    import sys
    pohja.destroy()
    sys.exit(0)
def hätä():
    print("Hätä. Apu on tulossa!")
def kutsu():
    print("Tulemme käymään mahdollisimman pian.")
def kyllä():
    print("Kyllä")
def ei():
    print("En")


pohja = tkinter.Tk()
pohja.title("Senior Notification Interface")

label = tkinter.Label(pohja,text="HEI. ONKO KAIKKI HYVIN?")
label.pack()

lopeta = tkinter.Button(pohja, text = "QUIT", command=lopeta)
lopeta.pack(side = BOTTOM)

hätä = tkinter.Button(pohja, text = "HÄTÄ", command=hätä)
hätä.bind("e", hätä)
hätä.place(relx=0.45, rely=0.5, anchor=CENTER)

kutsu = tkinter.Button(pohja, text = "KUTSU", command=kutsu)
kutsu.place(relx=0.35, rely=0.5, anchor=CENTER)
    
kyllä = tkinter.Button(pohja, text = "KYLLÄ", command=kyllä)
kyllä.place(relx=0.55, rely=0.5, anchor=CENTER)

ei = tkinter.Button(pohja, text = "EI", command=ei)
ei.place(relx=0.65, rely=0.5, anchor=CENTER)

pohja.mainloop()

