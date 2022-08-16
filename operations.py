import json
import os

chemin = os.path.dirname(os.path.abspath(__file__))
#print(chemin)
with open(f"{chemin}/liste.json", "r") as f:
    data = json.load(f)
data.append("cra")
with open (f"{chemin}/liste.json", "w") as f:
    json.dump(data, f)
print(data) 