def est_maj(age):
    if age >= 18:
        return True
    return False
    
def print_nom_age(nom, age):
    print(f"Age de {nom} est {age}")
    print(f"le nom possede {len(nom)} caracteres")

def recup_nom_personne(numero_personne): #numero_personne - parametre str ou int
    nom_de_pers = input(f"entrez le nom {numero_personne} :     ")
    age_de_pers = input(f"entrer age de personne {numero_personne}  :   ")
    return nom_de_pers, int(age_de_pers) #return le nom et l'age en INT

def recup_et_affiche_infos_personne(numero_personne):
    nom_pers, age_pers = recup_nom_personne(numero_personne) #prends les variables de recup_nom_personne
    print_nom_age(nom_pers, age_pers)
    if est_maj(age_pers):
        print("il est majeur")
    else:
        print("il est mineur")

nombre_de_personnes = 2   
for i in range(nombre_de_personnes):
    recup_et_affiche_infos_personne(i+1)

