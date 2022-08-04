a = input ("nom 1 : ")
b = input ("nom 2 : ")

if not (a.isdigit() and b.isdigit()):
    print ("it's not an number")
else:
    print(f"le resultat de l'addition de {a} + {b} = {int(a) + int(b)}")