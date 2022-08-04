
from random import randint

joueur_1 = 20
joueur_2 = 20
potions = 3

while joueur_1 >= 0 or joueur_2 >= 0:
    user_choise = input(" tu veux attaquer (1) ou prendre une potion (2) ?   ")

    

    if user_choise == "1":
        joueur_2 -= randint(5, 10)
        joueur_1 -= randint(5, 15)
 

    elif user_choise == "2" and potions > 0:
        joueur_1 += randint(5, 30)
        joueur_1 -= randint(5, 15)
        potions -= 1

    print(f"il vous reste {joueur_1} point")
    print(f"il reste a l'adversaire {joueur_2} point")
    print(f"il vous reste {potions} potions")


    if joueur_1 <= 0:
        print("tu as perdu")
        break
    elif joueur_2 <=0:
        print("tu as gagne")
        break

print("fin du jeu")     