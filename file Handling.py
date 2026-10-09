#What is a file?

#A file is a place where information is stored permanently.







#A file has two main actions:
#Open it
#Do something with it
#Close it

#Like a book:


#fil= open ("note.text")

password = input("Enter password:" )

file = open("attempt.text", "a")    #This tells python to open the file call "attempt.text" and create it iff doesn't exist for adding information
file.write(password + "\n")        #This tells to store the password in the file attempt.text.
                                 #"/n" means start with a new line
file.close()             #this means close the file after saved.

if password.endswith ("345"):
    print("Correct")

else:
    print("Wrong")



file = open("attempt.text", "r")

content = (file.read())

print(content)

file.close()