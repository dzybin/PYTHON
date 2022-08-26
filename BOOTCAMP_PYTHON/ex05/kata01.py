
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

text_to_insert = "was created by"

'''for key in kata.keys():
    print(key)'''
keys = kata.keys()  # method "keys" to get keys
print(keys)

value = kata.values() #method "values" to get values
print(value)

for key, value in kata.items(): #method "items" to get key and values
    print(f"{key} {text_to_insert} {value}")
