#store = ["Pasta", "Candy", "chocolate",]      # The list is a box

#for y in store:                               #Python opens the box and takes out one item at a time.
   # print(y)



#foods = ["Rice", "Candy", "Pizza", "Candy", "Burger"]

#for y in foods:
    #if y == "Candy":
    #    continue
    #print(y)


#numbers = [2, 5, 8, 11, 14, 17]
#for y in numbers:
 #   if y == 5:           # this is a great thinking but What if the list had 100 odd numbers?
  #      continue         # that would be a challenge, here is an easy short cut   if y % 2 != 0:
   # continue
    #if y == 11:
     #   continue
    #if y == 17:
     #   continue
   # print(y)


    #rewritten code

#numbers = [2, 5, 8, 11, 14, 17]

#for y in numbers:
 #       if y % 2 != 0:
  #          continue
   #     print(y)



#LAST CHALLENGE OF LOOPS WITH LISTS

names = ["Ali", "Hassan", "Ahmed", "Fatima", "Amina"]

for people in names:
    if people [0] != "A":
        continue
    print(people)

