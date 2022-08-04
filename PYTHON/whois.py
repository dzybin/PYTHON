import sys

number = int(sys.argv[1])

if (number % 2 == 0 and number != 0):
    print("even")
elif (number == 0):
    print ("ZERO")
else:
    print ("odd")