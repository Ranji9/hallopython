import time
import webbrowser
Learnzeit = input("bitte gib dein Learnzeit ein: ")
Pausenzeit = input("bitte gib dein Pausenzeit ein: ")
print("ich arbeite " +  Learnzeit + " Sekunden")
time.sleep (int(Learnzeit))
print("du hast  " + Pausenzeit + "Sekunden")
webbrowser.open("https://www.youtube.com/watch?v=wXjhszy2f9w")
time.sleep (int(Pausenzeit))
