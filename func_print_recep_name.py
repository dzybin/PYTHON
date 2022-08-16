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

def print_recepies_names():
    key = list(cookbook.keys())
    for i, element in enumerate(key,1):
        print(i, element)
print_recepies_names()
