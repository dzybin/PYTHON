import datetime
kata = (2019, 9, 25, 3, 30)

liste_kata = list(kata) #convert to liste

liste_kata = liste_kata [1], liste_kata[2], liste_kata[0],liste_kata[3], liste_kata[4] #put on wanted order

liste_kata = list(liste_kata) # convert tp list

#date1 = datetime.date(liste_kata)
print(f"0{liste_kata[0]}/{liste_kata[1]}/{liste_kata[2]} 0{liste_kata[3]}:{liste_kata[4]}")

