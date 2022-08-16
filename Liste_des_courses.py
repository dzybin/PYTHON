import os
import json


user_input = ""
new_liste = []
j = 1
chemin = os.path.dirname(os.path.abspath(__file__))

#if os.path.exists("liste.json"):
choix = [
    " Ajouter",
    " Supprimer", 
    " Afficher", 
    " Vider", 
    " Quitter"
]

while user_input != str(6) and user_input not in range(1,6):
    for i, element in enumerate(choix, 1):
        print(f"{i}. {element}")

    user_input = input("faites un choix :")
    
    if user_input == str(1):
        new_element = input("add to the list : ")
        new_liste.append(new_element)
        print(f"Un element {new_element} a ete rajoute ")
    elif user_input == str(2):
        removed_element = input("remove from liste : ")
        #if not new
        new_liste.remove(removed_element)
        print(f"Element {removed_element} a ete retire")
    elif user_input == str(3):
        if not new_liste:
            print("rien dans la liste")
        else:
            for j, item in enumerate(new_liste, 1):
                    print(f"{j}.{item}")
    elif user_input == str(4):
        del new_liste
        print("votre liste a ete supprime")
    elif user_input == str(5):
        if (os.path.exists(f"{chemin}/test.json")):
            with open(f"{chemin}/test.json", "r") as f:
                donnees = json.load(f)
            donnees.append(new_liste)
            with open(f"{chemin}/test.json", "w") as f:
                json.dump(donnees, f)
            print(donnees) 
        
    #else:
    #    print("sortir")
