mdp = input("Entrez un mot de pass (min 8 caracteres) : ")
mdp_trop_court = "votre mot de pass est trop court."

if(len(mdp) == 0):
    print(mdp_trop_court.swapcase())
elif not len(mdp) == 0 and len(mdp) < 8 :
    print(mdp_trop_court.capitalize())
elif(mdp.isnumeric()):
    print("Votre mot de passe ne contient que des nombres")
else:
    print("Inscription terminee")

