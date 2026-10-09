print(" ----Student Manager-----")


print("1. Add student")
print("2. View students")
print("3. Find student")
print("Exit")

Students = [{"name": "Hassan", "Grade": "8th grade", "Age": "14 years old",}, 
            {"name": "Ahmed", "Grade": "9th grade", "Age": "15 years old"}, 
            {"name": "Abdiwaasac", "Grade": "9th grader", "Age": "15 years old"}]




choice = input("Enter your choice(1-3):")

file = open("store.txt", "a")


if choice == "1":
    name =input("What is your name?")

    file.write(name + "\n")
    file.close()

    file = open("store.txt", "a")

    grade = input("What is your grade?")

    file.write(grade + "\n")

    file.close()

    file = open("store.txt", "a")
    try:
        Age = int (input("What is your age?"))
        file.write(str(Age) + "\n")
        print ("Thank you! Your response is saved")

    except ValueError:
        print ("Please enter your age in numbers only")

    file.close()
    
elif choice == "2":
    for x in Students:
        print(x)
elif choice == "3":
        question = input("What is the name of the student your searching?")

        found = False

        for y in Students:
         if y ["name"] == question:
            print("Yes, we do have that student in our data")
            found = True

        if found == False:
         print("No, we don't have that student")

else:
    print("Goodbye")

       