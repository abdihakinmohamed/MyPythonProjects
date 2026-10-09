12

import random

number = random.randint(1,100)

#print(number)

attempt = 1
question = int(input("Guess the number"))

file = open("tries.text" , "a")

file.write (str(question) + "\n")

file.close ()


if question == number:
  print("Correct")
elif question < number:
   print("Too low")

elif question > number:
   print("Too high")

while question != number:
   question = int(input("Guess the number"  ))

   attempt += 1
   file = open ("tries.text", "a")
   file.write(str(question) + "\n")
   file.close ()
   if question == number:
    print ("Correct")
   elif question > number:
     print("Below")
   elif question < number:
    print("Above")
  
file = open ("tries.text", "r")
store = (file.read())
print(store)
file.close()
print ("Attempts::", attempt)