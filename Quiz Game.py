print ("This Quiz is about waking you up to reality after you experienced a lot of time you spent scrolling")
print ("----Hit the Quiz----")


answer = 355
country = "China"
score = 0
earth = 4.5

question1 = int(input("How many days are in the Hijir Calender?"))


while answer != question1:
    question1 = int(input("Try again:    "))

print("Excellent")

score += 1

remainder =int(input("How many hours do you spend scrolling?"))

if remainder <6:
    print("Try to reduce an hour per day")
elif remainder >=6:
     print ("You neeed an emergency")


question2 = input("Where is Tiktok owned from?")

while question2 != country:
   question2 = input ("One More time?")

print("Correct")
score +=1



remainder1 = input("Have you ever go out to think freely?")

if remainder1 == "yes":
    print("Congratualtions, you ae truly a human.")

elif remainder1 == "no":
    print("Come back to humanity")

question3 = float(input("How old is Earth, according to scientists, in billion years?"))

while question3 != earth:
    question3 = float (input("Try again:    "))

print ("Amazing")

score += 1

print (score)

    