import random
number_of_try = 1
random_number = random.randint(0,10)
while number_of_try <= 5:
    guess_number = int(input("Votre valeur :"))
    if guess_number == random_number:
        print(f"tu as gagne en {number_of_try} essais")
        break
    elif guess_number <= random_number:
        print(f"""votre valeur est inferieur au nombre cherche
                il vous reste {5 - number_of_try} essais""")
    elif guess_number >= random_number:
        print(f"""votre valeur est superieur au nombre cherche
                il vous reste {5 - number_of_try} essais""") 
    if number_of_try == 5:
        print("tu as perdu")
    number_of_try += 1
