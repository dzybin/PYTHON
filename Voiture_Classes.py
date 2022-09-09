from dataclasses import dataclass

@dataclass  #DECORATOR
class Voiture:
    roule : int
    essence: int


    def afficher_reservoir(essence):
        print(f"La voiture contient {essence}")
    #roule = Voiture.roule = 5*50/100
    #essence = Voiture.essence

    def rouler (essence, km):
        essence -= (km*5)/100
        print (f"il reste {essence} L dans le reservoir")
    rouler (100, 30)
    rouler(96.5, 30)