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

def delete_recepe():
    """key = list(cookbook.keys())
    for i, element in enumerate(key,1):
        print(i, element)"""
    element_to_remove = input(" taper le nom de recette a supprimer   ")
    cookbook.pop(element_to_remove)
    print(cookbook)
    
delete_recepe()