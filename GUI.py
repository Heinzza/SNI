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

pvm = Label(pohja,text="Päivämäärä tähän", font=("Arial",11))
pvm.pack()
pvm.place(relx=0.05, rely=0.04, anchor=S)
pvm.config(background="grey")

huone = Label(pohja, text="Huonenumero tähän", font=("Arial",11))
huone.pack()
huone.place(relx=0.055, rely=0.07, anchor=S)
huone.config(background="grey")


label = Label(pohja,text="HEI. ONKO KAIKKI HYVIN?",font=("Arial",28))
label.pack()
label.config(background = "grey")
label.place(relx=0.5, rely=0.15, anchor=CENTER)
label.config(height=10,width=30) 


lopeta = Button(pohja, text = "QUIT", command=lopeta)
lopeta.pack(side = BOTTOM)
lopeta.configure(background='grey')
lopeta.config(height=1,width=6)
lopeta.config(font="bold")


kutsuteksti = Label(pohja, text="Paina 1 lähettääksesi",font=("Arial",13))
kutsuteksti.pack()
kutsuteksti.config(height=2,width=20)
kutsuteksti.config(background = "grey")
kutsuteksti.place(relx=0.2, rely=0.4, anchor=CENTER)
kutsu = Button(pohja, text = "KUTSU", font=("Arial",20), command=kutsu)
kutsu.place(relx=0.2, rely=0.5, anchor=CENTER)
pohja.bind("1", ku)
kutsu.config( height = 3, width = 9)
kutsu.configure(background='green')



hätäteksti = Label(pohja, text="Paina 2 lähettääksesi",font=("Arial",13))
hätäteksti.pack()
hätäteksti.config(height=2,width=20)
hätäteksti.config(background = "grey")
hätäteksti.place(relx=0.4, rely=0.4, anchor=CENTER)
hätä = Button(pohja, text = "HÄTÄ", font=("Arial",20), command=hätä)
hätä.place(relx=0.4, rely=0.5, anchor=CENTER)
pohja.bind("2", hä)
hätä.config( height = 3, width = 9)
hätä.configure(background='red')


    
kylläteksti = Label(pohja, text="Paina 3 vastataksesi",font=("Arial",13))
kylläteksti.pack()
kylläteksti.config(height=2,width=20)
kylläteksti.config(background = "grey")
kylläteksti.place(relx=0.6, rely=0.4, anchor=CENTER)
kyllä = Button(pohja, text = "KYLLÄ",font=("Arial",20),command=kyllä)
kyllä.place(relx=0.6, rely=0.5, anchor=CENTER)
pohja.bind("3", ky)
kyllä.config( height = 3, width = 9)
kyllä.configure(background='green')



eiteksti = Label(pohja, text="Paina 4 vastataksesi",font=("Arial",13))
eiteksti.pack()
eiteksti.config(height=2,width=20)
eiteksti.config(background = "grey")
eiteksti.place(relx=0.8, rely=0.4, anchor=CENTER)
ei = Button(pohja, text = "EI",font=("Arial",20), command=ei)
ei.place(relx=0.8, rely=0.5, anchor=CENTER)
pohja.bind("4", e)
ei.config( height = 3, width = 9)
ei.configure(background='red')




pohja.mainloop()
