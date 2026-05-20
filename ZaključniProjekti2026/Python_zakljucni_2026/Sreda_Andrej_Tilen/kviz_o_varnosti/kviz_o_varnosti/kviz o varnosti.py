#kviz o varnosti
import tkinter as tk
from PIL import ImageTk, Image # za branje slik

from tkinter import NW

trenutni_korak = 0
zgodovina = []

zgodba = [
    
    [ #vprasanje 1
    "Ali delimo gesla s prijatelji?",
    "Ja", 1,
    "Ne", 2
    ],
    [ #opcija 1 - Napacna 
    "Ne, to ni pravilno.",
    "Nadaljuj...", 3,
    None,
    None
    
    ],
    [ #opcija 2 - Pravilna 
    "Pravilno!",
    "Nadaljuj...", 3,
    None,
    None,
    None
    ],
    [ #vprasanje 2
    "Katero geslo je bolj varno?",
    "MojaMucaTiana", 4,   # napačno
    "Y~Hs887{T", 5        # pravilno
    ],
    [
    "Ne, to ni varno geslo.",
    "Nadaljuj...", 6,
    None, None
    ],
    [
    "Pravilno!",
    "Nadaljuj...", 6,
    None, None
    ],
    

    [ #vprasanje 3
    "Kaj naredis, ce dobis sumljiv email z tipko - klikni tukaj?",
    "Kliknes tipko", 7,
    "Ne kliknes tipke in poves odrasli osebi", 8
    ],
    [
    "Ne, to ni varno.",
    "Nadaljuj...", 9,
    None, None
    ],
    [
    "Pravilno!",
    "Nadaljuj...", 9,
    None, None
    ],
   #vprasanje 4
    [
    "Če te neznanec na spletu doda kot prijatelja, ali sprejmeš?",
    "Ja.", 10,
    "Ne.", 11
    ],
    [
    "Ne, to ni vredu.",
    "Nadaljuj...", 12,
    None, None
    ],
    [
    "Pravilno!",
    "Nadaljuj...", 12,
    None, None
    ],
    #vprasanje 5
    [
    "Ali delimo osebne podatke z neznanci na spletu?",
    "Ne", 14,
    "Ja", 13
    ],
    [
    "Ne, to ni varno.",
    "Nadaljuj...", 15,
    None, None
    ],
    [
    "Pravilno!",
    "Nadaljuj...", 15,
    None, None
    ],
    [
    "Bravo, zakljuil/a si s kvizom.",
    None,
    None,
    None,
    None
    ]
]

def nazaj():
    if zgodovina:
        prejsnji = zgodovina.pop()
        prikazi_korak(prejsnji)

def naslednji(korak):
    zgodovina.append(trenutni_korak)
    prikazi_korak(korak)

def naredi_ukaz(korak):
    def ukaz():
        naslednji(korak)
    return ukaz

def prikazi_korak(i):
    global trenutni_korak
    global zgodba

    trenutni_korak = i
    korak = zgodba[i]

    label.config(text=korak[0])
    gumb_nazaj.pack_forget()

    #img1 = Image.open('slike/poletje.jpg') # pot do datoteke
    #resized_img1 = img1.resize((300, 200))
    # povemo novo velikost (x,y)
    #new_img1 = ImageTk.PhotoImage(resized_img1)
    # naša nova slika, ki je lahko prilepljena na platno
    #canvas = tk.Canvas(frame2, width=315, height=215)
    # na katerem oknu ga bomo imeli, velikost
    #label_image.config(image=new_img1)
    #label_image.image = new_img1
    
    #gumb 1
    if korak[1] != None:
        gumb1.config(text=korak[1], command=naredi_ukaz(korak[2]))
        gumb1.pack()
    else:
        gumb1.pack_forget()

    #gumb2
    if korak[3] != None:
        gumb2.config(text=korak[3], command=naredi_ukaz(korak[4]))
        gumb2.pack()
    else:
        gumb2.pack_forget()
    ###
    gumb_nazaj.pack()

#okno tkinter
root = tk.Tk()
root.geometry("400x400")
frame1 = tk.Frame(root, width=400, height=200)
frame1.pack()

label = tk.Label(frame1, text="", wraplength=300)
label.pack()

gumb1 = tk.Button(frame1)
gumb1.pack()

gumb2 = tk.Button(frame1)
gumb2.pack()

gumb_nazaj = tk.Button(frame1, text="Nazaj", command=nazaj)


# SLIKA V TKINTER
#frame2 = tk.Frame(root,width=400, height=250)
#frame2.pack()
#img1 = Image.open('slike/zima.jpg') # pot do datoteke
#resized_img1 = img1.resize((300, 200))
# povemo novo velikost (x,y)
#new_img1 = ImageTk.PhotoImage(resized_img1)
# naša nova slika, ki je lahko prilepljena na platno
#canvas = tk.Canvas(frame2, width=315, height=215)
# na katerem oknu ga bomo imeli, velikost
#canvas.create_image(15, 15, anchor=NW, image=new_img1)
# prilepimo sliko na platno # x, y koordinate, kam ga zasidramo-povemo kje se usede - # absolutna pozicija, povemo še katero sliko prilepimo
#canvas.place(x=50, y=55)
#label_image = tk.Label(frame2, image=new_img1)
#label_image.pack()

prikazi_korak(0)

#tk.Button(root, text="Nazaj", command=nazaj).pack()

root.mainloop()