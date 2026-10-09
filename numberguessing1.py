

print("Guessing number game")


number = 234
#hint = (number /2)

question = int(input("Guess the number"))



if question == (number):
    print ("Correct")

else:

    question1 = input("Do you want a hint? (yes/no):")
    if question1 == "yes":
        print("It starts with 2 and ends with 4")



    if question1 == "no":
      while question != number:
           print("Wrong")
           question = int(input("Guess the number:   "))
    print("correct")





#def loop():
 #   print(question)

#question1 = input("no")
##if question1 == "no":
#loop()









    #if question1 == "yes":
     #   print(hint)








    #if question1 == "yes":
               # for x in question1:
                     #  print("It starts with 2 and ends with 4")




#if x in question == ("yes"):




  #  print("Wrong")



   # for x in question1:
   #     if x == ("yes"):
     #       continue


#while number >= 200:
   # print("You are very close")

  #  number = number + 1



          