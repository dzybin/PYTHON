import os
import json
import sys # pour quitter le programe

chemin = os.path.dirname(__file__) # chemin vers le dossier parent
file_place = os.path.join(chemin, "liste.json") # chemin vers le fichier

if os.path.exists(file_place):
    with open (file_place, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []
while True:
    user_choise = input("faites votre chois  ")
    if user_choise == "1":
        new_entry = input("add a new item   ")

        LISTE.append(new_entry)
    elif user_choise == "5":
        with open(file_place, "w") as f:
            json.dump(LISTE, f, indent=4)
            break
print (LISTE)


