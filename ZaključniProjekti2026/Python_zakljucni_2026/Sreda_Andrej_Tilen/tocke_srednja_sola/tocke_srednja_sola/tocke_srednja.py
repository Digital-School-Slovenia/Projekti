import pygame
from tkinter import *
from tkinter import messagebox
from turtle import *
import sys
import tkinter as tk
import math
mreza = [[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None],[None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None, None, None, None ,None, None, None, None]]

root = tk.Tk()
root.configure(background='lightblue')
root.title("Računanje točk za NPZ")
root.option_add("*Label.Background", "lightblue")
root.option_add("*Entry.Background", "lightgrey")
root.option_add("*Entry.BorderWidth", "1")
root.option_add("*Entry.Relief", "ridge")
root.option_add("*Button.Background", "lightgrey")


tocke = tk.Label(root)
ni_predmeta = tk.StringVar(value="NI PREDMETA")
pet = tk.IntVar(value="5")
pet2 = tk.IntVar(value="5")
pet3 = tk.IntVar(value="5")
pet4 = tk.IntVar(value="5")
pet5 = tk.IntVar(value="5")
pet6 = tk.IntVar(value="5")
pet7 = tk.IntVar(value="5")
pet8 = tk.IntVar(value="5")
pet9 = tk.IntVar(value="5")
pet10 = tk.IntVar(value="5")
pet11 = tk.IntVar(value="5")
pet12 = tk.IntVar(value="5")
pet13 = tk.IntVar(value="5")
pet14 = tk.IntVar(value="5")
pet15 = tk.IntVar(value="5")
pet16 = tk.IntVar(value="5")
pet17 = tk.IntVar(value="5")
pet18 = tk.IntVar(value="5")
pet19 = tk.IntVar(value="5")
pet20 = tk.IntVar(value="5")
pet21 = tk.IntVar(value="5")
pet22 = tk.IntVar(value="5")
pet23 = tk.IntVar(value="5")
pet24 = tk.IntVar(value="5")
pet25 = tk.IntVar(value="5")
pet26 = tk.IntVar(value="5")
pet27 = tk.IntVar(value="5")
pet28 = tk.IntVar(value="5")
pet29 = tk.IntVar(value="5")
pet30 = tk.IntVar(value="5")
pet31 = tk.IntVar(value="5")
pet32 = tk.IntVar(value="5")
pet33 = tk.IntVar(value="5")
pet34 = tk.IntVar(value="5")
pet35 = tk.IntVar(value="5")
pet36 = tk.IntVar(value="5")
pet37 = tk.IntVar(value="5")
pet38 = tk.IntVar(value="5")
pet39 = tk.IntVar(value="100")
pet40 = tk.IntVar(value="100")


label = tk.Label(root, text="Tukaj lahko vpišete svoje ocene in NPZ rezultate ter izveste svoje točke za srednjo šolo!", font=('Arial', 15))
label.grid(row=0, column=1, columnspan=3, sticky="n")


label1 = tk.Label(root, text="")
mreza[1][0] = label1
label1.grid(row=1, column=0, sticky="n")

label2 = tk.Label(root, text="7. Razred", width=9)
mreza[1][1] = label2
label2.grid(row=1, column=1, sticky="n", padx=10, pady=10)

label3 = tk.Label(root, text="8. Razred", width=9)
mreza[1][2] = label3
label3.grid(row=1, column=2, sticky="n", padx=10, pady=10)

label4 = tk.Label(root, text="9. Razred", width=9)
mreza[1][3] = label4
label4.grid(row=1, column=3, sticky="n", padx=10, pady=10)

label5 = tk.Label(root, text="NPZ", width=9)
mreza[1][4] = label5
label5.grid(row=1, column=4, sticky="n", padx=10, pady=10)

slo = tk.Label(root, text="SLO", width=3)
mreza[2][0] = slo
slo.grid(row=2, column=0, sticky="n", padx=10, pady=10)

input1 = tk.Entry(root, textvariable=pet)
mreza[2][1] =input1
input1.grid(row=2, column=1, sticky="n", padx=10, pady=10)


input2 = tk.Entry(root, textvariable=pet2)
mreza[2][2] =input2
input2.grid(row=2, column=2, sticky="n", padx=10, pady=10)

input3 = tk.Entry(root, textvariable=pet3)
mreza[2][3] =input3
input3.grid(row=2, column=3, sticky="n", padx=10, pady=10)

input4 = tk.Entry(root, textvariable=pet40)
mreza[2][4] =input4
input4.grid(row=2, column=4, sticky="n", padx=10, pady=10)

mat = tk.Label(root, text="MAT", width=3)
mreza[3][0] = mat
mat.grid(row=3, column=0, sticky="n", padx=10, pady=10)

inputmat1 = tk.Entry(root, textvariable=pet4)
mreza[3][1] =inputmat1
inputmat1.grid(row=3, column=1, sticky="n", padx=10, pady=10)

inputmat2 = tk.Entry(root, textvariable=pet5)
mreza[3][2] =inputmat2
inputmat2.grid(row=3, column=2, sticky="n", padx=10, pady=10)

inputmat3 = tk.Entry(root, textvariable=pet6)
mreza[3][3] =inputmat3
inputmat3.grid(row=3, column=3, sticky="n", padx=10, pady=10)

inputmat4 = tk.Entry(root, textvariable=pet39)
mreza[3][4] =inputmat4
inputmat4.grid(row=3, column=4, sticky="n", padx=10, pady=10)

tja = tk.Label(root, text="TJA", width=3)
mreza[4][0] = tja
tja.grid(row=4, column=0, sticky="n", padx=10, pady=10)

inputtja1 = tk.Entry(root, textvariable=pet7)
mreza[4][1] =inputtja1
inputtja1.grid(row=4, column=1, sticky="n", padx=10, pady=10)

inputtja2 = tk.Entry(root, textvariable=pet8)
mreza[4][2] =inputtja2
inputtja2.grid(row=4, column=2, sticky="n", padx=10, pady=10)

inputtja3 = tk.Entry(root, textvariable=pet9)
mreza[4][3] =inputtja3
inputtja3.grid(row=4, column=3, sticky="n", padx=10, pady=10)

lum = tk.Label(root, text="LUM", width=3)
mreza[5][0] = lum
lum.grid(row=5, column=0, sticky="n", padx=10, pady=10)

inputlum1 = tk.Entry(root, textvariable=pet10)
mreza[5][1] =inputlum1
inputlum1.grid(row=5, column=1, sticky="n", padx=10, pady=10)

inputlum2 = tk.Entry(root, textvariable=pet11)
mreza[5][2] =inputlum2
inputlum2.grid(row=5, column=2, sticky="n", padx=10, pady=10)

inputlum3 = tk.Entry(root, textvariable=pet12)
mreza[5][3] =inputlum3
inputlum3.grid(row=5, column=3, sticky="n", padx=10, pady=10)

gum = tk.Label(root, text="GUM", width=3)
mreza[6][0] = gum
gum.grid(row=6, column=0, sticky="n", padx=10, pady=10)

inputgum1 = tk.Entry(root, textvariable=pet13)
mreza[6][1] =inputgum1
inputgum1.grid(row=6, column=1, sticky="n", padx=10, pady=10)

inputgum2 = tk.Entry(root, textvariable=pet14)
mreza[6][2] =inputgum2
inputgum2.grid(row=6, column=2, sticky="n", padx=10, pady=10)

inputgum3 = tk.Entry(root, textvariable=pet15)
mreza[6][3] =inputgum3
inputgum3.grid(row=6, column=3, sticky="n", padx=10, pady=10)

geo = tk.Label(root, text="GEO", width=3)
mreza[7][0] = geo
geo.grid(row=7, column=0, sticky="n", padx=10, pady=10)

inputgeo1 = tk.Entry(root, textvariable=pet16)
mreza[7][1] =inputgeo1
inputgeo1.grid(row=7, column=1, sticky="n", padx=10, pady=10)

inputgeo2 = tk.Entry(root, textvariable=pet17)
mreza[7][2] =inputgeo2
inputgeo2.grid(row=7, column=2, sticky="n", padx=10, pady=10)

inputgeo3 = tk.Entry(root, textvariable=pet18)
mreza[7][3] =inputgeo3
inputgeo3.grid(row=7, column=3, sticky="n", padx=10, pady=10)

zgo = tk.Label(root, text="ZGO", width=3)
mreza[8][0] = zgo
zgo.grid(row=8, column=0, sticky="n", padx=10, pady=10)

inputzgo1 = tk.Entry(root, textvariable=pet19)
mreza[8][1] =inputzgo1
inputzgo1.grid(row=8, column=1, sticky="n", padx=10, pady=10)

inputzgo2 = tk.Entry(root, textvariable=pet20)
mreza[8][2] =inputzgo2
inputzgo2.grid(row=8, column=2, sticky="n", padx=10, pady=10)

inputzgo3 = tk.Entry(root, textvariable=pet21)
mreza[8][3] =inputzgo3
inputzgo3.grid(row=8, column=3, sticky="n", padx=10, pady=10)

dke = tk.Label(root, text="DKE", width=3)
mreza[9][0] = dke
dke.grid(row=9, column=0, sticky="n", padx=10, pady=10)

inputdke1 = tk.Entry(root, textvariable=pet22)
mreza[9][1] =inputdke1
inputdke1.grid(row=9, column=1, sticky="n", padx=10, pady=10)

inputdke2 = tk.Entry(root, textvariable=pet24)
mreza[9][2] =inputdke2
inputdke2.grid(row=9, column=2, sticky="n", padx=10, pady=10)

inputdke3 = tk.Label(root, textvariable=ni_predmeta)
mreza[9][3] = inputdke3
inputdke3.grid(row=9, column=3, sticky="n", padx=10, pady=10)

fiz = tk.Label(root, text="FIZ", width=3)
mreza[10][0] = fiz
fiz.grid(row=10, column=0, sticky="n", padx=10, pady=10)

inputfiz1 = tk.Label(root, textvariable=ni_predmeta)
mreza[10][1] =inputfiz1
inputfiz1.grid(row=10, column=1, sticky="n", padx=10, pady=10)

inputfiz2 = tk.Entry(root, textvariable=pet26)
mreza[10][2] =inputfiz2
inputfiz2.grid(row=10, column=2, sticky="n", padx=10, pady=10)

inputfiz3 = tk.Entry(root, textvariable=pet27)
mreza[10][3] =inputfiz3
inputfiz3.grid(row=10, column=3, sticky="n", padx=10, pady=10)

kem = tk.Label(root, text="KEM", width=3)
mreza[11][0] = kem
kem.grid(row=11, column=0, sticky="n", padx=10, pady=10)

inputkem1 = tk.Label(root, textvariable=ni_predmeta)
mreza[11][1] =inputkem1
inputkem1.grid(row=11, column=1, sticky="n", padx=10, pady=10)

inputkem2 = tk.Entry(root, textvariable=pet29)
mreza[11][2] =inputkem2
inputkem2.grid(row=11, column=2, sticky="n", padx=10, pady=10)

inputkem3 = tk.Entry(root, textvariable=pet30)
mreza[11][3] =inputkem3
inputkem3.grid(row=11, column=3, sticky="n", padx=10, pady=10)

bio = tk.Label(root, text="BIO", width=3)
mreza[12][0] = bio
bio.grid(row=12, column=0, sticky="n", padx=10, pady=10)

inputbio1 = tk.Label(root, textvariable=ni_predmeta)
mreza[12][1] =inputbio1
inputbio1.grid(row=12, column=1, sticky="n", padx=10, pady=10)

inputbio2 = tk.Entry(root, textvariable=pet31)
mreza[12][2] =inputbio2
inputbio2.grid(row=12, column=2, sticky="n", padx=10, pady=10)

inputbio3 = tk.Entry(root, textvariable=pet32)
mreza[12][3] =inputbio3
inputbio3.grid(row=12, column=3, sticky="n", padx=10, pady=10)

nar = tk.Label(root, text="NAR", width=3)
mreza[13][0] = nar
nar.grid(row=13, column=0, sticky="n", padx=10, pady=10)

inputnar1 = tk.Entry(root, textvariable=pet33)
mreza[13][1] =inputnar1
inputnar1.grid(row=13, column=1, sticky="n", padx=10, pady=10)

inputnar2 = tk.Label(root, textvariable=ni_predmeta)
mreza[13][2] =inputnar2
inputnar2.grid(row=13, column=2, sticky="n", padx=10, pady=10)

inputnar3 = tk.Label(root, textvariable=ni_predmeta)
mreza[13][3] =inputnar3
inputnar3.grid(row=13, column=3, sticky="n", padx=10, pady=10)

tit = tk.Label(root, text="TIT", width=3)
mreza[14][0] = tit
tit.grid(row=14, column=0, sticky="n", padx=10, pady=10)

inputtit1 = tk.Entry(root, textvariable=pet34)
mreza[14][1] =inputtit1
inputtit1.grid(row=14, column=1, sticky="n", padx=10, pady=10)

inputtit2 = tk.Entry(root, textvariable=pet35)
mreza[14][2] =inputtit2
inputtit2.grid(row=14, column=2, sticky="n", padx=10, pady=10)

inputtit3 = tk.Label(root, textvariable=ni_predmeta)
mreza[14][3] =inputtit3
inputtit3.grid(row=14, column=3, sticky="n", padx=10, pady=10)

špo = tk.Label(root, text="ŠPO", width=3)
mreza[15][0] = špo
špo.grid(row=15, column=0, sticky="n", padx=10, pady=10)

inputšpo1 = tk.Entry(root, textvariable=pet36)
mreza[15][1] =inputšpo1
inputšpo1.grid(row=15, column=1, sticky="n", padx=10, pady=10)

inputšpo2 = tk.Entry(root, textvariable=pet37)
mreza[15][2] =inputšpo2
inputšpo2.grid(row=15, column=2, sticky="n", padx=10, pady=10)

inputšpo3 = tk.Entry(root, textvariable=pet38)
mreza[15][3] =inputšpo3
inputšpo3.grid(row=15, column=3, sticky="n", padx=10, pady=10)

vse_tocke_60 = 0
    
i = 0
def oceneskupi():
    global tocke
    global i
    global vse_tocke_60
    global mreza
    vse_tocke = pet.get() + pet2.get() + pet3.get() + pet4.get() + pet5.get() + pet6.get() + pet7.get() + pet8.get() + pet9.get() + pet10.get() + pet11.get() + pet12.get() + pet13.get() + pet14.get() + pet15.get() + pet16.get() + pet17.get() + pet18.get() + pet19.get() + pet20.get() + pet21.get() + pet22.get() + pet24.get() + pet26.get() + pet27.get() + pet29.get() + pet30.get() + pet31.get() + pet32.get() + pet33.get() + pet34.get() + pet35.get() + pet36.get() + pet37.get() + pet38.get()
    
    vse_tocke_60 = vse_tocke * 12 / 35
    
    
    npzmat = pet39.get() / 5
    npzslj = pet40.get() / 5
    
    srednja = vse_tocke_60 + npzmat + npzslj

    if srednja > 100:
        srednja = 100
        srednja = "Vnesli ste prevelike ocene ali rezultate NPZ-ja"
        
    
    
    print(srednja)

    tocke.config(text=f"Točke: {srednja}")
    mreza[16][3] = tocke
    tocke.grid(row=16, column=3, sticky="n", padx=15, pady=15)
    srednja = 0


izracun = tk.Button(root, text="Izračun", font=('Arial', 13), width=6, height=1, command=oceneskupi)
mreza[16][2] = izracun
izracun.grid(row=16, column=2, sticky="n", padx=15, pady=15)


import pygame
from tkinter import *
from tkinter import messagebox
from turtle import *
import sys
root1 = Tk()
root1.title("TeachPY")
root1.configure(background='lightblue')
root1.option_add("*Button.Background", "lightgrey")

x = 0
y = 0





def leave():
    sys.exit()


def draw():
    def center_():
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
    def red_color():
        turtle.pencolor("red")
    def green_color():
        turtle.pencolor("green")
    def black_color():
        turtle.pencolor("black")
    def blue_color():
        turtle.pencolor("blue")
    def pen_up():
        turtle.penup()
    def pen_down():
        turtle.pendown()
    def erase_():
        x, y = turtle.pos()
        print(x)
        print(y)
        screen.reset()
        print(x)
        print(y)
        turtle.penup()
        turtle.speed(8)
        turtle.goto(x, y)
        turtle.pendown()


    draw_igra = Button(root1, text="Red", font=('Arial', 30), width=5, height=2, bg="#CF1616", command=red_color)
    mreza[1][0] = draw_igra
    draw_igra.grid(row=1, column=0, sticky=W, padx=15, pady=10)
    black = Button(root1, text="Black", font=('Arial', 30), width=5, height=2, bg="#000000",fg="white", command=black_color)
    mreza[1][1] = black
    black.grid(row=1, column=1, sticky=W, padx=15, pady=10)
    blue = Button(root1, text="Blue", font=('Arial', 30), width=5, height=2, bg="#295BA7",command=blue_color)
    mreza[1][2] = blue
    blue.grid(row=1, column=2, sticky=W, padx=15, pady=10)
    green = Button(root1, text="Green", font=('Arial', 30), width=5, height=2, bg="#17A51C",command=green_color)
    mreza[1][3] = green
    green.grid(row=1, column=3, sticky=W, padx=15, pady=10)
    penup = Button(root1, text="Pen Up", font=('Arial', 30), width=8, height=2, command=pen_up)
    mreza[2][0] = penup
    penup.grid(row=2, column=0, sticky=W, padx=10, pady=10)
    pendown = Button(root1, text="Pen Down", font=('Arial', 30), width=8, height=2, command=pen_down)
    mreza[2][2] = pendown
    pendown.grid(row=2, column=2, sticky=W, padx=10, pady=10)
    erase = Button(root1, text="Erase", font=('Arial', 30), width=8, height=2, command=erase_)
    mreza[2][1] = erase
    erase.grid(row=2, column=1, sticky=W, padx=15, pady=10)
    center = Button(root1, text="Center", font=('Arial', 30), width=8, height=2, command=center_)
    mreza[2][2] = center
    center.grid(row=2, column=3, sticky=W, padx=15, pady=10)
    turtle = Turtle()
    screen = Screen()
    turtle.speed(8)
    screen.onscreenclick(turtle.goto)
    turtle.getscreen()._root.mainloop()
    


draw_igra = Button(root1, text="Draw", font=('Arial', 30), width=5, height=2, command=draw)
mreza[1][1] = draw_igra
draw_igra.grid(row=1, column=1, sticky=W, padx=15, pady=10)


leave = Button(root1, text="Leave", font=('Arial', 30), width=5, height=2, command=leave)
mreza[0][1] = leave
leave.grid(row=0, column=1, sticky=W, padx=15, pady=10)



root1.mainloop()








draw()





