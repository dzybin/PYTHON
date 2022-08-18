cookbook = {
            "Sandwich": {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
                        "meal" : "lunch",
                        "prep_time" : 10
                        },
            "Cake":     {"ingredients" : ["flour", "sugar", "eggs"],
                        "meal" : "dessert",
                        "prep_time" : 60
                        },
            "Salad" :   {"ingredients" : ["avocado", "arugula", "tomatoe", "spinach"],
                        "meal" : "lunch",
                        "prep_time" : 15
                        }

            }

def add_new_recette():          
    recette_name = input("enrtrez le nom de la recette    ")
    cookbook[f"{recette_name}"] = {"ingredients": [], "meal" : "", "prep_time": 0}
    recette_ingredients = input("entrer les ingredients   ")
    cookbook[f"{recette_name}"]["ingredients"] = recette_ingredients
    meal_type = input("quel repas   ")
    cookbook[f"{recette_name}"]["meal"] = meal_type
    time_to_prepare = input("entrer le temps de preparation    ")
    cookbook[f"{recette_name}"]["prep_time"] = time_to_prepare

def delete_recepe():   
    element_to_remove = input(" taper le nom de recette a supprimer   ")
    cookbook.pop(element_to_remove)

def print_recepies_names():
    key = list(cookbook.keys())
    for i, element in enumerate(key,1):
        print(i, element)
    print("+" * 50)

def affiche_recette():
    key = list(cookbook.keys()) 
    recette_a_voir = input("Taper le nom de recette a afficher :  ")
    if recette_a_voir in key:
        print(f"les ingredients de {recette_a_voir} sont : {cookbook[recette_a_voir]['ingredients']}")
        print(f"on mange ceci en {cookbook[recette_a_voir]['meal']}")
        print(f"le temps de preparation est de {cookbook[recette_a_voir]['prep_time']} minutes")


    else:
        print(f"Veuillez rentrer un nom de recette compris dans {key}")

choix_fait = ""
element = ""
choix = ["Ajouter une recette",
        "Supprimer une recette",
        "Afficher une recette",
        "Afficher la liste de recettes",
        "Fermer le livre de recettes"
        ]
print("Bienvenue dans votre livre de recettes")
print()
print("*" * 50)
print()

while choix_fait != 3:
    for i, element in enumerate(choix, 1):
        print(f"{i}. {element}")
    print()
    print("*" * 76)

    choix_fait = input("Faites votre choix :")
    if choix_fait == "1":
        add_new_recette()
    elif choix_fait == "2":
        delete_recepe()
    elif choix_fait == "3":
        affiche_recette()
    elif choix_fait == "4":
        print_recepies_names()
    elif choix_fait == "5":
        print("A la prochaine")
        break
    


