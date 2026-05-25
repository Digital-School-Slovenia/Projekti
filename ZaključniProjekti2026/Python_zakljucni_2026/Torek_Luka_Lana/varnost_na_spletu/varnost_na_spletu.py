import random
import datetime

print("Pozdravljeni! Sem tvoj osebni chatbot in odgovorim na vsa vprašanja na temo varnosti na spletu")

ime = input("Živijo kako ti je ime? ")
print(f"Me veseli, {ime}! Jaz sem tvoj računalnik.")

def daj_geslo(): 
    seznam = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*_-+=čžšČŽŠ"
    geslo = ""
    dolzina = random.randint(12, 18)
    for ele in range(0, dolzina):
        geslo += random.choice(seznam)
    print("Primer gesla:", geslo)

while True:
    
    user_input = input("\nVprašaj me o varnosti na spletu: ").lower().strip()

    if user_input == "kaksno je dobro geslo ki ga lahko uporabim":
        print("Dobro geslo je dolgo, edinstveno in ima simbole.")
        if input("Ti pokazem primer? ").lower().strip() == "ja":
            daj_geslo()

    elif user_input == "kako se lahko zavarujem pred online prevarami":
        print("Ne deli podatkov in ne klikaj sumljivih linkov.")
        if input("Ti pokazem primer prevare? ").lower().strip() == "ja":
            print("Primer: https://brezplacni-vbucks-2026.si ")

    elif user_input == "zakaj tvoje geslo luka123 ni dobra ideja":
        print("Ker ga heker ugane v eni sekundi in je preveč enostavno.")

    elif user_input == "dobiš sms v njem piše klikni tu kaj naredim":
        print("Takoj ga zbriši in nikoli ne klini na povezavo.")

    elif user_input == "zakaj je javni wi-fi v kafiču nevaren":
        print("Ker lahko ljudje v istem omrežju vidijo, kaj počneš na netu.")

    
    elif user_input == "koliko je ura":
        print("Ura je:", datetime.datetime.now().strftime("%X"))

    elif user_input == "kako si":
        print("Super sem, ker sem v oblaku in mi ni treba v šolo.")

    
    elif user_input == "kaj se zgodi ce dam nekomu mojo davcno stevilko":
        print("Lahko ti ukradejo identiteto ali odprejo lažne račune na tvoje ime.")
    
    elif user_input == "kako se lahko na spletu zavarujem najbolje":
        print("Uporabljaj močna gesla in ne nasedaj na prevare. Ne deli svojih osebni podatkov. To so 3 ključne stvari ki so najbolj pomembne za varno rabo interneta.")

    elif user_input == "kaj se zgodi če dam prst v utičnco":
        print("Dobiš zaston rože. Ampak ne probavaj tega")

    elif user_input == "daj mi kratko vprašanje o geslu":

        print("Kaj je najbolj varno geslo?")
        print("1 - luka123")
        print("2 - password")
        print("3 - T7$kP!9xLm#2")

        odgovor = input("Tvoj odgovor: ")

        if odgovor == "3":
            print("Bravo ")

        else:
            print("Narobe ")

    elif user_input == "preveri moje geslo":

        geslo = input("Vpiši geslo: ")

        if len(geslo) < 8:
            print("Geslo je prekratko.")

        elif geslo.isalpha():
            print("Dodaj številke in simbole.")

        else:
            print("Geslo izgleda kar močno. ")


    
    else:
        print("Tega ne razumem, vprašaj chatgpt")
        
