import random

ordlista = ["ö", "å", 
            "te", "le", "ko", "rå", "ny", "öl", 
            "bil", "hus", "hej", "vin", "pil", "sko", 
            "katt", "hund", "skog", "pool", "bygg", "moln",
            "äpple", "skola", "köket", "havet", "cykel", "pojke"]

fel_gissningar = []
antal_gissningar = 10

ord = random.choice(ordlista)
bokstäver = list(ord)
while antal_gissningar != 0:
    print("_ " * len(bokstäver))
    gissning = input("Ange en bokstav: ")

    if gissning in bokstäver:
        print(True)

    if gissning not in bokstäver:
        fel_gissningar.append(gissning)
        print(fel_gissningar)
        antal_gissningar -= 1
        print("Antal gissningar kvar: ", antal_gissningar)
