#String methods

#definition =  String methods are built-in functions that work with strings. 
# They can change the text, 
# search it, split it, count parts of it, or perform other operations.

#BUILT IN FUNCTION: means something that python have like ".upper()"
#we don't have to write that because python has for us.

#Example:

#name = "Abdihakin"
#print(name.upper())


#BUT LOOK AT THIS:

#name = "Abdihakin"
#name.upper()              #This is just "Abdihakin" with no capital letters because you didn't run the upper()
#print(name)                #You didn't run it as the above example


#Here it is the BUILT IN FUNCTIONS for string methods

#.upper()
#.lower()
#.title()        Makes the first letter of each word uppercase.
#.capitalize()   Makes only the first letter of the sentence uppercase.
#.strip()        Removes spaces from the beginning and end.
#.replace()      Replaces one text with another.
#.split()        Splits a sentence into a list of words.
#.find()       Finds the position of a letter or word.
#.count()       Counts how many times a letter or word appears.
#.startswith()      Checks if the text starts with something.
#.endswith()        Checks if the text ends with something.

#Example for Capitalise

#name = "abdihakin"           #capitalsises the first letter.
#print(name.capitalize())




#name ="abdihakin"         
#print(name.startswith("abd"))   # tells true or fals



#name = "abdihakin"           
#print(name.count("b"))  only 1 b is there





#name = "abdihakin"           
#print(name.find("n"))    n is the 8th letter





#name = "abdihakin"           
#print(name.replace("n", "w"))        replaced n to w





#name = "abdihakin"           
#print(name.endswith("n"))       # tells if the last letter is



name = "I am Abdihakin"

word = name.split()

print(word)


#Test

#text = "I love Java"
#print(text.replace("Java", "Python"))


