import random

ordlista = ["ö", "å", 
            "te", "le", "ko", "rå", "ny", "öl", 
            "bil", "hus", "hej", "vin", "pil", "sko", 
            "katt", "hund", "skog", "pool", "bygg", "moln",
            "äpple", "skola", "köket", "havet", "cykel", "pojke", 
            "blomma", "socker", "färger", "rummet", "låtsas", "spring",
            "apelsin", "elefant", "fönster", "klockan", "telefon", "grönsak",
            "ryggsäck", "stjärnor", "regnbåge", "teckning", "rullstol", "lekplats",
            "skrivbord", "flygplats", "kylskåpet", "tidningar", "veckopeng", "bokhandel"]

fel_gissningar = []
antal_gissningar = 10

ord = random.choice(ordlista)
bokstäver = list(ord)
luckor = ["_"] * len(bokstäver)

while antal_gissningar > 0:
    print(luckor)

    if "_" not in luckor:
        print("Du hittade ordet!🎉")
        print("Du använde", 10 - antal_gissningar, "/ 10 gissningar.")
        break

    gissning = input("Ange en bokstav: ").lower()

    if gissning in fel_gissningar:
        print("Du har redan gissat på denna bokstav.")

    elif gissning in bokstäver:
        for i, bokstav in enumerate(bokstäver):
            if gissning == bokstav:
                print("Hittade: ", gissning)
                luckor[i] = gissning

    elif gissning not in bokstäver:
        fel_gissningar.append(gissning)
        print(fel_gissningar)
        antal_gissningar -= 1
        print("Gissningar kvar: ", antal_gissningar)

    if antal_gissningar == 0:
        print("Du har inga gissningar kvar, du förlorade.🥀")
        print("Ordet var: ", ord)