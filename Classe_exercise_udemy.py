class Livre:
    def __init__(self,nom, nombre_de_pages, prix): #initialisation des instances
        #assignation des valeurs aux instances 
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix
## Creation des instances a partir de la classe Livre avec des valeurs differentes
livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le Seigneur des Anneaux", 400, 13.99)

print(livre_HP.nom, livre_HP.nombre_de_pages, livre_HP.prix)