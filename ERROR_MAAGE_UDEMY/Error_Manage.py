fichier = input("entrez le chemin du fichier a ouvrir :")

try: 
    f = open(fichier, "r")
    print(f.read())
except FileNotFoundError:
    print ("pas de fichier")
except UnicodeDecodeError:
    print ("s'ouvre pas")
else:
    f.close()