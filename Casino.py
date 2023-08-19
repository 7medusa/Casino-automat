import random
score = 12
bilder = ["platin", "diamant", "gold", "eisen", "bronze", "holz"]def zufall():
        global zufall1
        global zufall2
        global zufall3
        zufall1 = random.choice(bilder)
        zufall2 = random.choice(bilder)
        zufall3 = random.choice(bilder)
def vergleich():
        global score
        print(f"{zufall1} {zufall2} {zufall3}")
        if zufall1 == "platin" and zufall2 == "platin" and zufall3 == "platin":
                print("jackpot")
                score = score + 10
        if zufall1 == zufall2 == zufall3:
                print("alle gleich")
                score = score + 5
        elif zufall1 == zufall2 or zufall1 == zufall3 or zufall2 == zufall3:
                print("zwei gleich")
                score = score + 2
        else:
                print("nichts")
while score > 0:
        eingabe = int(input(">"))
        if eingabe == 1:
                score = score - 1
                zufall()
                vergleich()
                print(f"Guthaben: {score}")
                eingabe = 0
        elif eingabe == 2:
                exit()
        elif score == 100:
                print("gewonnen")
        else:
                print("fehler")
print("verloren")
