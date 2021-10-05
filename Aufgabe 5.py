import random
print("zahlenraten")

versuche=6
zufallszahl = random.randint(1,100)
while versuche >0:
    versuche-=1
    a=input("zahl eingeben ")
    b=int(a)
    if zufallszahl <b:
        print("zu hoch!!!!!")
    if zufallszahl > b:
        print("Zu niedrig, du Landratte")
    elif zufallszahl==b:
        print(" glückwünch,du hast richtige Zahl erraten")
        print("du hattest noch "+str(versuche)+ "versuche übrig"   )
        break
        print("du hattest noch "+str(versuche)+ "versuche übrig"   )
    if versuche == 0:
        print("Game over")    