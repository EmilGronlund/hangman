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
rätt_gissningar = []
antal_gissningar = 8

ord = random.choice(ordlista)
bokstäver = list(ord)
luckor = ["_"] * len(bokstäver)

while True:
    print(" ".join(luckor))

    if "_" not in luckor:
        print("Du hittade ordet!🎉")
        print("Du använde", 8 - antal_gissningar, "/ 8 gissningar.")
        fråga = input("Vill du spela igen? (j/n): ").lower()
        if fråga == "n":
            print("Spelet har avslutats.")
            break
        else:
            fel_gissningar = []
            rätt_gissningar = []
            antal_gissningar = 8
            ord = random.choice(ordlista)
            bokstäver = list(ord)
            luckor = ["_"] * len(bokstäver)
            continue

    gissning = input("Ange en bokstav: ").lower()

    if gissning in fel_gissningar or gissning in rätt_gissningar:
        print("Du har redan gissat på denna bokstav.")

    elif not gissning.isalpha():
        print("Din gissning kan endast innehålla bokstäver.")

    elif len(gissning) > 1:
        print("Du kan endast gissa på 1 bokstav.")

    elif gissning in bokstäver:
        rätt_gissningar.append(gissning)
        for i, bokstav in enumerate(bokstäver):
            if gissning == bokstav:
                print("Hittade: ", gissning)
                luckor[i] = gissning

    else:
        fel_gissningar.append(gissning)
        print(fel_gissningar)
        antal_gissningar -= 1
        print("Gissningar kvar: ", antal_gissningar)

    if antal_gissningar == 0:
        print("Du har inga gissningar kvar, du förlorade.🥀")
        print("Ordet var: ", ord)
        fråga = input("Vill du spela igen? (j/n): ").lower()
        if fråga == "n":
            print("Spelet har avslutats.")
            break
        else:
            fel_gissningar = []
            rätt_gissningar = []
            antal_gissningar = 8
            ord = random.choice(ordlista)
            bokstäver = list(ord)
            luckor = ["_"] * len(bokstäver)
            continue
