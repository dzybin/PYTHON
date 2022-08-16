import json
import os
#chemin = "/Users/minor/PycharmProjects/pythonProject13/test.json"
chemin = os.path.dirname(os.path.abspath(__file__))
print (chemin)
print(os.path.exists(f"{chemin}/test.json"))

#with open(chemin, "w") as f:
#    json.dump("bob", f)
"""with open("data.json", "r") as f:
    #file openning in read mode
    donnees = json.load(f)
    #reading the file and putting its content in variable "donnees"
donnees.append(4)
    #adding a value

donnees = ["coucou", "coco"]
with open("liste.json", "w") as f:
    #openning in write mode
    json.dump("donnees", f, indent=4)
    #writing the new data in json file
    print(f)"""
