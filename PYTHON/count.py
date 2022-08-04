import sys
import string

phrase = sys.argv[1]
count_punct = 0
count_upper = 0
count_lower = 0
count_space = 0
for i in phrase:
    if i in string.punctuation:
        count_punct = count_punct + 1
    elif(i.islower()):
        count_lower = count_lower + 1
    elif(i.isupper):
        count_upper = count_upper + 1
    elif i == " ":
        count_space = count_space + 1
print(count_punct)
print(count_lower)
print(count_upper)
#print(count_space)
"""for letter in phrase:
    if letter == letter.upper:
        count_upper = count_upper + 1

print (count_upper)
"""
