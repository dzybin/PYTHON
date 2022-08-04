def balance_list_int(lst_int: list) -> int:    
    resultat = -1
    for i in range(0, len(lst_int)):
        aleft = 0
        aright = 0
        for j in range (0, i+1):
            aleft += lst_int[j]
        for j in range(i + 1, len(lst_int)):
            aright += lst_int[j]
        if aleft == aright:
            resultat = i
            print(resultat)
            exit()
    print(resultat)


#lst_int = [1, 5, 0, 9, 1, 2, 8, 6]
lst_int = [1, 1, 2]
balance_list_int(lst_int)