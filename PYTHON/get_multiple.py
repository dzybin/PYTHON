def sum_of_multiple_3_5(n: int) -> int:
    """ Coder votre fonction ici.
    """
    resultat = 0
    for i in range(1, n):
        if i %3 == 0 or i%5 == 0 and i < n:
            resultat += i
    print (resultat)

sum_of_multiple_3_5(15)