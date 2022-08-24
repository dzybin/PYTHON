import string


def filterwords(string_to_filter, number_of_characters):
    if len(locals()) > max_arg: #chcks if number of argumenys is less than max_arg
        print("Error, too many arguments")
        return
        
    if type(number_of_characters) is int and type(string_to_filter) is str:
        string_to_filter = string_to_filter.translate(str.maketrans("", "", string.punctuation))
        """str.maketrans creates a dictionary to be replaced by 'None' all stuff which is in string.punctuation
            #punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''"""
        liste_string = string_to_filter.split() # splits sring in words and makes a list
        final_liste = (words for words in liste_string if len(words) > number_of_characters) #puts words bigger than argument in the variable
        print (list(final_liste))
    else:
        print("Error, please enter a valid value")

    
#string_to_filter = "Je ne veux pas travailler, ,,,!! []"
max_arg = 2
string_to_filter = "Je, ne?? ??veux!! pas><<>travailler"
number_of_characters = 2
filterwords(string_to_filter, number_of_characters)


