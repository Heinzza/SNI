import tkinter

print("Hello!")
print("Senior Notification Interface")

c = "Kutsu. Tulemme mahdollisimman pian."

e = "Hätä! Apu on tulossa."

y = "OK, hyvä."

n = "Nyt saatana!"

m = "Oletko ottanut lääkkeesi?"

root = tkinter.Tk()
root.title("Senior Notification Interface")
label = tkinter.Label(root,text="Mitä asiaa?")
eka = input(":")
while eka == "c" or "e":
    if eka == "c":
        print(c)
    elif eka == "e":
        varma = input("Oletko varma, että haluat lähettää hätäkutsun? :")
        if varma == "e":
            print(e)        
    else:
        if eka == "m":
            toka = input(m + ": ")
            if toka == "y":
                print(y)
            elif toka == "n":
                print(n)
    eka = input(":")
root.mainloop() 



 
    
