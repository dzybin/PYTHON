import pprint

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

pprint.pprint(cookbook)

# Sets "pretty_dict_str" to
#pretty_dict_str = pprint.pformat(cookbook)
#print(pretty_dict_str)

"""def afficher_recette():           
    #chois = input("taper le nom de recette   ")
    for key, value in cookbook.items():
        
        print("{} ({})".format(key, value))
    #print(f"La recette de {chois} est :  {cookbook.get(chois)}")
afficher_recette()   """ 


