import time
import webbrowser
import random
Learnzeit = input("bitte gib dein Learnzeit ein: ")
Pausenzeit = input("bitte gib dein Pausenzeit ein: ")
print("ich arbeite " +  Learnzeit + " Sekunden")
time.sleep (int(Learnzeit))
print("du hast  " + Pausenzeit + "Sekunden")
webbrowser.open("https://www.youtube.com/watch?v=wXjhszy2f9w")
time.sleep (int(Pausenzeit))
Warmeup=input("Brauchst du Warme-up? :")
if Warmeup == "ja":
    print("Zahlenratesspieln")
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
