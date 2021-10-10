import time
import webbrowser
Learnzeit_counter=0
Pausenzeit_counter=0
Lerngesamtzeit=0
Pausengesamtzeit=0
while Lerngesamtzeit < 28800:
    Learnzeit = input("bitte gib dein Learnzeit ein: ")
    Pausenzeit = input("bitte gib dein Pausenzeit ein: ")
    print("ich arbeite " +  Learnzeit + " Sekunden")
    time.sleep (int(Learnzeit))
    Lerngesamtzeit = Lerngesamtzeit+int(Learnzeit)
    Learnzeit_counter = Learnzeit_counter + 1
    print("du hast  " + Pausenzeit + "Sekunden pause")
    webbrowser.open("https://www.youtube.com/watch?v=wXjhszy2f9w")
    time.sleep (int(Pausenzeit))
    Pausengesamtzeit = Pausengesamtzeit +int(Pausenzeit)
    Pausenzeit_counter = Pausenzeit_counter + 1
    print("wieviel mal habe ich Pause genommen  " + str(Pausenzeit_counter) )
    print("wieviel mal habe ich Learnzeit gehabt  " + str(Learnzeit_counter) )