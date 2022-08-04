def square_digit(n) -> int:
    s = ''
    for i in str(n):
        #y = (int(n)**2)
        s += str(int(i)**2)
    print(int(s))

square_digit(245)