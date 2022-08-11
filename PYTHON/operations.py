
a = 5
b = 0

if type(a) != int:
    print("it's not a number")
elif type(b) != int:
     print("it's not a number") 
elif b == 0:
    print ("division by 0")
else:
    sum = a + b
    print(f"somme : {sum}")
    dif = a - b
    print(f"soustraction : {dif}")

