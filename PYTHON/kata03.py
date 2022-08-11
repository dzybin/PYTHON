kata = "The right format"

longueur = len(kata)
traits = 42 - longueur -1 #pas compris pourquoi wc -c retourne 
                            #un byte de plus
print(f"{'-'*traits}{kata}")

