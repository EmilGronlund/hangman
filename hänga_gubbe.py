import random

ordlista = ["kalender", "fotograf", "applåder", "trädgård", "semester", "slutföra", 
            "barnbarn", "katterna", "tandvård", "sjukvård", "långsamt", "kattunge", 
            "förtjust", "skolbänk", "hundarna", "matbutik", "stadshus", "hotellet"]

ord = random.choice(ordlista)
bokstäver = list(ord)
luckor = ("_ _ _ _ _ _ _ _")
print(luckor)
gissning = input("Ange en bokstav: ")
if gissning in bokstäver:
    bokstäver.index(gissning)
else:
    print(luckor)