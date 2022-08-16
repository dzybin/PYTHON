cookbook = {
            "Sandwich": {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
                        "meal" : "lunch",
                        "prep_time" : 10
                        },
            "Cake":     {"ingredients" : ["flour", "sugar", "eggs"],
                        "meal" : "desert",
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
    #print(cookbook)

#add_new_recette()
"""def remove_item(item):
    item = cookbook.pop("Cake")
    for key, value in cookbook.items():
        print(key, value)
    return (key, value)
print(remove_item)"""
