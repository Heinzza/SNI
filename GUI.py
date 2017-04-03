import tkinter
from tkinter import *

def lopeta():
    import sys
    pohja.destroy()
    sys.exit(0)

def hätä():
    print("Hätä. Apu on tulossa!")
def hä(hätä):
    print("Hätä. Apu on tulossa!")
        
def kutsu():
    print("Tulemme käymään mahdollisimman pian.")
def ku(kutsu):
    print("Tulemme käymään mahdollisimman pian.")

def kyllä():
    print("Kyllä")
def ky(kyllä):
    print("Kyllä")

def ei():
    print("En")
def e(ei):
    print("En")


pohja = tkinter.Tk()
pohja.title("Senior Notification Interface")
pohja.configure(background='grey')


label = tkinter.Label(pohja,text="HEI. ONKO KAIKKI HYVIN?")
label.pack()
label.config(background = "grey")

label.config(height=10,width=200) 
label.configure(font="bold")
 

lopeta = tkinter.Button(pohja, text = "QUIT", command=lopeta)
lopeta.pack(side = BOTTOM)
lopeta.configure(background='grey')


kutsu = tkinter.Button(pohja, text = "KUTSU", command=kutsu)
kutsu.place(relx=0.35, rely=0.5, anchor=CENTER)
pohja.bind("1", ku)
kutsu.config( height = 6, width = 13)
kutsu.configure(background='green')
kutsu.configure(font="bold")


hätä = tkinter.Button(pohja, text = "HÄTÄ", command=hätä)
hätä.place(relx=0.45, rely=0.5, anchor=CENTER)
pohja.bind("2", hä)
hätä.config( height = 6, width = 13)
hätä.configure(background='red')
hätä.configure(font="bold")

    
kyllä = tkinter.Button(pohja, text = "KYLLÄ", command=kyllä)
kyllä.place(relx=0.55, rely=0.5, anchor=CENTER)
pohja.bind("3", ky)
kyllä.config( height = 6, width = 13)
kyllä.configure(background='green')
kyllä.configure(font="bold")


ei = tkinter.Button(pohja, text = "EI", command=ei)
ei.place(relx=0.65, rely=0.5, anchor=CENTER)
pohja.bind("4", e)
ei.config( height = 6, width = 13)
ei.configure(background='red')
ei.configure(font="bold")

pohja.mainloop()

