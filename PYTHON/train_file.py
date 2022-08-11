import os
import json

CUR_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(CUR_DIR, "new_liste.json")


if os.path.exists(FILE_PATH):
    with open (FILE_PATH, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []

while True:
    user_choise = input("votre choix    ")
    if user_choise == "1":
        new_item = input("etrez un item   :")

        LISTE.append(new_item)

    elif user_choise == "5":
        with open (FILE_PATH, "w") as f:
            json.dump(LISTE, f, indent = 4)
        break
    print(LISTE)




