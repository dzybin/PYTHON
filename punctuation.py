import string
string_to_filter = 'je ne veux, [qs tra'
translator = str.maketrans('','',string.punctuation)
string_to_filter = string_to_filter.translate(translator)
print (string_to_filter)
print(string.punctuation)