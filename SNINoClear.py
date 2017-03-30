print("Hello!")
print("Senior Notification Interface")

c = "Kutsu. Tulemme mahdollisimman pian."

e = "Hätä! Apu on tulossa."

y = "OK, hyvä."

n = "Nyt saatana!"

m = "Oletko ottanut lääkkeesi?"


eka = input(":")
while eka == "c" or "e":
    if eka == "c":
        print(c)
    elif eka == "e":
        print(e)
    else:
        if eka == "m":
            toka = input(m + ": ")
            if toka == "y":
                print(y)
            elif toka == "n":
                print(n)
    eka = input(":")
    
