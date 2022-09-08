from dataclasses import dataclass

@dataclass  #DECORATOR
class Voiture:
    essence: int
    def roule():
        km_roule = input("nombre des km parcourus :  ")
benzin = Voiture(essence = 100)
print(benzin.essence)

