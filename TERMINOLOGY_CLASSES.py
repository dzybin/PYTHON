from decimal import ROUND_CEILING


class Voiture: # CLASS
    voiture_couleur = "rouge" #ATTRIBUT DE CLASSE
    voiture_count = 0           #ATTRIBUT DE CLASSE

    def __init__(self, marque):  #METHODE
        self.marque = marque        #ATTRIBUT D'INSTANCE
        Voiture.voiture_count += 1

voiture_01 = Voiture("koum")  #INSTANCE
voiture_02 = Voiture("wroum")

print(voiture_01.marque)
print(voiture_01.voiture_couleur)
print(Voiture.voiture_count)

class Livre:
    def __init__ (self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix
livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le Seigneur des Anneaux", 400, 13.99)

print(livre_HP.nom, livre_HP.nombre_de_pages)