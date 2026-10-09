#1. EXAMPLE

#try:
   # age = int(input("Enter your age"))      #if the user enters a age in texts, there will be an error. because this
   # print(age)                             #this only need numbers. 

#except:                                      #but in order to tell the user write in numbers use (try) and (except)
   # age= int(input("Please enter your age in numbers!"))
  #  print(age)




#2. Another example

#number = 10 /0
#print(number)     #This says: ZeroDivisionError, which can't be divided to 0. 
                  #but you can prevent this by using try and except

                  #Here is the correct

try:
    number = 10 /0

except: ZeroDivisionError
print("Wrong divisor")   #keep in mind you can use another except with another error name like
                      #ValueError, but python only runs what is needed to fix the situation.
                      #ValueError, is used to solve like example 1.
                      # 
           
           
           
            #else can also be used like this


try:
    number = int(input("Enter a number: "))

except ValueError:
    print("That is not a number")

else:
    print("good")

