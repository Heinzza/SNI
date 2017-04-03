#!/usr/bin/python 3
import sys
from tkinter import *

def lopeta():
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


pohja = Tk()
pohja.title("Senior Notification Interface")
pohja.configure(background='grey')


label = Label(pohja,text="HEI. ONKO KAIKKI HYVIN?")
label.pack()
label.config(background = "grey")
label.config(height=10,width=200) 
label.configure(font="bold")

 

lopeta = Button(pohja, text = "QUIT", command=lopeta)
lopeta.pack(side = BOTTOM)
lopeta.configure(background='grey')
lopeta.config(height=1,width=6)
lopeta.config(font="bold")


kutsuteksti = Label(pohja, text="Paina 1 lähettääksesi")
kutsuteksti.pack()
kutsuteksti.config(height=2,width=20)
kutsuteksti.config(background = "grey")
kutsuteksti.place(relx=0.35, rely=0.4, anchor=CENTER)
kutsu = Button(pohja, text = "KUTSU", command=kutsu)
kutsu.place(relx=0.35, rely=0.5, anchor=CENTER)
pohja.bind("1", ku)
kutsu.config( height = 6, width = 13)
kutsu.configure(background='green')
kutsu.configure(font="bold")


hätäteksti = Label(pohja, text="Paina 2 lähettääksesi")
hätäteksti.pack()
hätäteksti.config(height=2,width=20)
hätäteksti.config(background = "grey")
hätäteksti.place(relx=0.45, rely=0.4, anchor=CENTER)
hätä = Button(pohja, text = "HÄTÄ", command=hätä)
hätä.place(relx=0.45, rely=0.5, anchor=CENTER)
pohja.bind("2", hä)
hätä.config( height = 6, width = 13)
hätä.configure(background='red')
hätä.configure(font="bold")

    
kylläteksti = Label(pohja, text="Paina 3 vastataksesi")
kylläteksti.pack()
kylläteksti.config(height=2,width=20)
kylläteksti.config(background = "grey")
kylläteksti.place(relx=0.55, rely=0.4, anchor=CENTER)
kyllä = Button(pohja, text = "KYLLÄ", command=kyllä)
kyllä.place(relx=0.55, rely=0.5, anchor=CENTER)
pohja.bind("3", ky)
kyllä.config( height = 6, width = 13)
kyllä.configure(background='green')
kyllä.configure(font="bold")


eiteksti = Label(pohja, text="Paina 4 vastataksesi")
eiteksti.pack()
eiteksti.config(height=2,width=20)
eiteksti.config(background = "grey")
eiteksti.place(relx=0.65, rely=0.4, anchor=CENTER)
ei = Button(pohja, text = "EI", command=ei)
ei.place(relx=0.65, rely=0.5, anchor=CENTER)
pohja.bind("4", e)
ei.config( height = 6, width = 13)
ei.configure(background='red')
ei.configure(font="bold")



pohja.mainloop()

