import time

#
#Quinn Bellamy Hartwell - inteligentna, tiha, natančna
#Mireille Sinclair – skrivnostna, očarljiva, preračunljiva
#Rosalie Lovewood – prijazna, naivna, čustvena
#Ella Caldyn – samozavestna, impulzivna, neposredna
#Max Anderson – ciničen, opazovalen, zadržan
#Timothy Carter – živčen, radoveden, nezanesljiv 
#Zgodba:


liki = ["Quinn Bellamy Hartwell", "Mireille Sinclair", "Rosalie Lovewood", "Ella Caldyn", "Max Anderson", "Timothy Carter"]
opisi = ["inteligentna, tiha, natančna", "skrivnostna, očarljiva, preračunljiva", "prijazna, naivna, čustvena", "samozavestna, impulzivna, neposredna", "ciničen, opazovalen, zadržan", "živčen, radoveden, nezanesljiv"]
print("Dobrodošli v Murder Mystery-ju!")
print()

print("Na voljo so:")
for i in range(6):
    print(f"{i+1}.) {liki[i]} ")
print()

while True:
    lik = int(input("Vnesi številko lika, katerega želiš igrati: "))
    if lik <= 6  or lik > 0:
        print(f"Izbral si {liki[lik-1]} - {opisi[lik-1]}")
        print()
        break
    else:
        print("Števila mora biti med 1 in 5")
        print()


main = liki[lik-1]
liki.pop(lik-1)
opisi.pop(lik-1)

time.sleep(3)

print("Greš na poletni tabor. Tam spoznaš Marka Richarda, ", end = " ")
for clan in liki:
    print(f"{clan}, ", end = " ")
    
print("v sobi si lahko z:")
for i in range(5):
    print(f"{i+1}.) {liki[i]} ")
print()

while True:
    lik = int(input("Vnesi številko lika, s katerim želiš biti v sobi: "))
    if lik <= 5 or lik > 0:
        print(f"Izbral si {liki[lik-1]} - {opisi[lik-1]}")
        break
    else:
        print("Število mora biti med 1 in 6")   

time.sleep(3)
        
print()
print("Cilj tabora je da, se naučiš osnove python-a.")
print()
time.sleep(3)
print()
print("Zaslišiš krik iz gozda in pritečeš, da ugotoviš kaj se je zgodilo. Vse kar vidiš je krvavo truplo enega od tabornikov. Ugotoviš, da je to Mark iz sosednje sobe.")

time.sleep(3)

print("Odločiš se raziskati umor. Tega ne boš nikomur povedal/-a.  Med listi grmovja najdeš zataknjen list. Na njemu piše: \"Če želiš izvedeti kdo je ubil Marka, moraš pravilno odgovoriti na vprašanja in dobil/-a boš zloge mojega imena.\"")
print()

while(True):
    print("1. vprašanje - Katerega leta je začel nastajati python?")
    print("1) 1967")
    print("2) 1999")
    print("3) 1989")
    prvo_vprasanje = input("Vpiši številko pred pravilnim odgovorom: ")
    if prvo_vprasanje == "3":
        print()
        print("Prvi zlog mojega imena je \"Co\".")
        time.sleep(3)
        break
    else:
        print("Ojoj nisi odgovoril/-a pravilno, poskusi še enkrat!")
        print()

print()
print("Ko prideš nazaj v hiško opaziš dvignjeno desko. Obrneš desko in vanj je vrezano naslednje vprašanje.")
print()

while(True):
    print("2. vprašanje")
    print("tabela = [4, 5, 6, 7, 8]")
    print("izracun = tabela[1] + tabela[4]")
    print("print(izracun)")
    drugo_vprašanje = input("Kakšen rezultat se bo izpisal? ")
    print()
    if drugo_vprašanje == "13":
        print("Drugi zlog mojega imena je \"le\".")
        break
    else:
        print("Nič ne veš o pythonu. SRAM TE BODI!!!!!!!!")
        print()

print()
print("Star računalnik na mizi se prižge. Izpiše se koda, ampak ne dela pravilno. Sklepaš, da je naslednji namig povezan z napako v kodi.")
print()

while(True):
    print("3. vprašanje")
    print("for i in range(3)")
    print("    print(\"Hello world!\")")
    print()
    tretje_vprašanje = input("Kaj manjka v kodi? ")

    print()

    if tretje_vprašanje == ":":
        print("Tretji zlog mojega imena je \"op\".")
        break
    else:
        print("BOLJ SE POTRUDI!!!!!!")
        print()


print()

print()
print("Zaslišiš nekakšen pok. Približaš se oknu in vidiš da se je zaletel ptič. Na nogi ima zvit kos papirja.")
time.sleep(3)
print("Vzameš kos papirja in spustiš ptiča ven iz hiške. Na papirju prebereš:\"Vem, da iščeš krivca za umor enega od tabornikov. Če želiš najti krivca, pravilno odgovori na naslednje vprasanje in bil/-a boš en korak bližje rezultatu")
print()

time.sleep(4)
while(True):
    print("4. vprašanje - Kdaj so v računalniku prvič našli hrošča/bug?")
    print("1) 1974")
    print("2) 1968")
    print("3) 1977")
    
    
    
    četrto_vprašanje = input("Izpiši število pred pravilnim odgovorom: ")
    print()

    if četrto_vprašanje == "1":
        print("Četrti zlog mojega imena je \"te\"")
        break
    else:
        print("Napačen odgovor. Naslednjič se bolj portudi!")
        print()

time.sleep(3)

print()
print("V enem od dveh hodnikov pred sabo zaslišiš svoje ime.")
hodniki = input("V katerega od hodnikov greš (desni ali levi)? ")
if hodniki == "desni":
    print("Stopiš v desni hodnik.")
    print("Nekaj časa hodiš, nato zaslišiš kapljanje vode. Pogledaš dol.")
    time.sleep(2)
    print("V luži pod sabo zagledaš svoj odsev, ter nekaj napisano na strop.")
    print("Pogledaš gor. Tam piše:")
else:
    print("Stopiš v levi hodnik.")
    print("Nekaj časa hodiš, nato naletiš na vrsto kamenčkov, razporejenih v besedilo.")
    time.sleep(3)
    print("Vendar ne moreš prebrati, kaj piše. Ugotoviš, da je zapisano zrcalno.")
    print(" Po naključju imaš v žepu ogledalo. Po nekaj časa ugotoviš, da piše:")
print()
time.sleep(2)
while(True):
    print("5. vprašanje")
    print("izracun = 5 + 3")
    print("if izracun > 8:")
    print("    print(java)")
    print("else:")
    print("    print(python)")
    print()
    time.sleep(3)
    peto_vprašanje = input("Kaj bo izpisala ta koda? ")
    if peto_vprašanje == "python":
        print("Peti zlog mojega imena je \"ra\"")
        break
    else:
        print("Kako tega ne veš?! Poskusi znova!")
        print()
    
    time.sleep(3)

print("Med reševanjem nalog in odgovarjanjem vprašanj si ob pravilnem odgovoru dobil/a zloge na listkih. Tvoja naloga je, da združiš vse zloge in ugotoviš rešitev.")
print("Pazi, če napačno odgovoriš... ")
time.sleep(4)
zadnje_vprašanje = input("Kdo sem? ")
if zadnje_vprašanje == "Coleoptera":
    time.sleep(3)
    print("Bravo! Rešil/-a si umor! Coleoptera je latinsko ime za hrošča, tako da je Marka ubil hrošč!")
    print()

    time.sleep(3)
                                                                                                                                
    print("Ugotovil/a si da je morilec hrošč. Odločiš se da boš pokončal hrošča, zato da nebi delal več težav na taboru. Natančno in previdno preglej kodo.")

    print("Če narobe odgovoriš bo hrošč zbežal.")
    time.sleep(2)

    print("Koda ima tri napake. Najdi jih in zapiši številko vrstic v kateri se napaka nahaja.")
    time.sleep(1)
    print("seznam = [5, 1, 3, 4] (1. vrstica)")
    print("indeks = 1 (2. vrstica)")
    print("vsota = 0 (3. vrstica)")
    print("while indeks <= 4: (4. vrstica)")
    print("vsota += seznam[indeks] (5. vrstica)")
    print("    indeks += 1 (6. vrstica)")
    print("print(vsota) (7. vrstica)")

    odgovor = input("Vpiši številke vrstic, kjer meniš, da je napaka. Vpiši številke v naraščajočem zaporedju in v formatu [1 2 3]: ")

    if odgovor == "2 4 5":
        print("Uspešno si pohodil hrošča in tabor je rešen! Vsi so veseli, da si rešil ta skrivnostni umor in ti v tvojo čast priredili zabavo!")
    else:
        print("Hrošč je nažalost zbežal, se vidimo naslednje leto. Spet.")
else:
    print("Joj, napačen odgovor! Zaradi tega si bil/-a umorjen/-a.")
 


