def filterwords(string, number_of_characters):

    
    liste_string = string.split() # splits sring in words and makes a list
    final_liste = (words for words in liste_string if len(words) > number_of_characters) #puts words bigger than argument in the variable
    print (list(final_liste))
    
string = "Je ne veux pas travailler"
number_of_characters = 3 
filterwords(string, number_of_characters)


