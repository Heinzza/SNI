#!/usr/bin/env python3
import sys
import datetime
from tkinter import *

def lopeta():
    pohja.destroy()
    sys.exit(0) #lopeta, ei virheitä

def hätä():
    print("Hätä. Apu on tulossa!")
def hätäKbd(hätä):
    print("Hätä. Apu on tulossa!")
    hätä = Toplevel()
    hätä.title("hätä")
    Message(hätä, text="Hätäkutsu on lähetetty, tulemme mahdollisimman pian", font=("Arial",20), padx=50, pady=50).pack()
    hätä.after(4000, hätä.destroy)
    hätä.geometry("300x200+540+300")

    


def kutsu():
    print("Tulemme käymään mahdollisimman pian.")
def kutsuKdb(kutsu):
    print("Tulemme käymään mahdollisimman pian.")
    kutsu = Toplevel()
    kutsu.title("Kutsu")
    Message(kutsu, text="Kutsu on lähetetty, tulemme mahdollisimman pian", font=("Arial",20), padx=50, pady=50).pack()
    kutsu.after(4000, kutsu.destroy)
    kutsu.geometry("300x200+540+300")


def kyllä():
    print("Kyllä")
def kylläKbd(kyllä):
    print("Kyllä")
    kyllä = Toplevel()
    kyllä.title("Kyllä")
    Message(kyllä, text="Vastasit kyllä", font=("Arial",20), padx=60, pady=60).pack()
    kyllä.after(4000, kyllä.destroy)
    kyllä.geometry("300x200+540+300")
    

def ei():
    print("En")
def eiKbd(ei):
    print("En")
    ei = Toplevel()
    ei.title("Ei")
    Message(ei, text="Vastasit ei", font=("Arial",20), padx=60, pady=60).pack()
    ei.after(4000, ei.destroy)
    ei.geometry("300x200+540+300")
    
#Luodaan tyhjä ikkuna
pohja = Tk()
pohja.title("Senior Notification Interface")
pohja.configure(bg='grey')
pohja.geometry("1350x730+2+1")


sni = Label(pohja, text="Senior Notification Interface", font=("Arial",20))
sni.pack
sni.config(bg="grey")
sni.place(relx=0.5, rely=0.04, anchor=CENTER)
sni.config(height=2,width=30)

#lisätään pävämäärä ja huonenumero
nyt = str(datetime.date.today())
pvm = Label(pohja,text="Päivämäärä: %s" % (nyt), font=("Arial",11))
pvm.pack()
pvm.place(relx=0.05, rely=0.04, anchor=S)
pvm.config(bg="grey")

huone = Label(pohja, text="Huonenumero tähän", font=("Arial",11))
huone.pack()
huone.place(relx=0.055, rely=0.07, anchor=S)
huone.config(bg="grey")


label = Label(pohja,text="HEI. ONKO KAIKKI HYVIN?",font=("Arial",30))
label.pack()
label.config(bg = "grey")
label.place(relx=0.5, rely=0.15, anchor=CENTER)
label.config(height=2,width=30) 

#Lopetus-nappi
lopeta = Button(pohja, text = "Quit", command=lopeta)
lopeta.pack(side = BOTTOM)
lopeta.configure(bg='grey')
lopeta.config(height=1,width=6)
lopeta.config(font="bold")

#Kutsu-nappi ja ohjeteksti
kutsuteksti = Label(pohja, text="Paina 1 lähettääksesi",font=("Arial",13))
kutsuteksti.pack()
kutsuteksti.config(height=2,width=20)
kutsuteksti.config(bg = "grey")
kutsuteksti.place(relx=0.2, rely=0.4, anchor=CENTER)
kutsu = Button(pohja, text = "KUTSU", font=("Arial",20), command=kutsu)
kutsu.place(relx=0.2, rely=0.5, anchor=CENTER)
pohja.bind("1", kutsuKdb) #Pikanäppäin, paina 1 -> Kutsu
kutsu.config( height = 3, width = 9)
kutsu.configure(bg='green')


#Hätä-nappi ja ohjeteksti
hätäteksti = Label(pohja, text="Paina 2 lähettääksesi",font=("Arial",13))
hätäteksti.pack()
hätäteksti.config(height=2,width=20)
hätäteksti.config(bg = "grey")
hätäteksti.place(relx=0.4, rely=0.4, anchor=CENTER)
hätä = Button(pohja, text = "HÄTÄ", font=("Arial",20), command=hätä)
hätä.place(relx=0.4, rely=0.5, anchor=CENTER)
pohja.bind("2", hätäKbd) #Pikanäppäin, paina 2 -> Hätä
hätä.config( height = 3, width = 9)
hätä.configure(bg='red')


#Kyllä-nappi ja ohjeteksti    
kylläteksti = Label(pohja, text="Paina 3 vastataksesi",font=("Arial",13))
kylläteksti.pack()
kylläteksti.config(height=2,width=20)
kylläteksti.config(bg = "grey")
kylläteksti.place(relx=0.6, rely=0.4, anchor=CENTER)
kyllä = Button(pohja, text = "KYLLÄ",font=("Arial",20),command=kyllä)
kyllä.place(relx=0.6, rely=0.5, anchor=CENTER)
pohja.bind("3", kylläKbd) #Pikanäppäin, paina 3 -> Kyllä
kyllä.config( height = 3, width = 9)
kyllä.configure(bg='green')


#Ei-nappi ja ohjeteksti
eiteksti = Label(pohja, text="Paina 4 vastataksesi",font=("Arial",13))
eiteksti.pack()
eiteksti.config(height=2,width=20)
eiteksti.config(bg = "grey")
eiteksti.place(relx=0.8, rely=0.4, anchor=CENTER)
ei = Button(pohja, text = "EI",font=("Arial",20), command=ei)
ei.place(relx=0.8, rely=0.5, anchor=CENTER)
pohja.bind("4", eiKbd) #Pikanäppäin, paina 4 -> Ei
ei.config( height = 3, width = 9)
ei.configure(bg='red')



pohja.mainloop()
