#person = [{"name": "Hassan", "age": "18", "school": "Ali dayib"}]
#print(person)



#students = [{"name": "Ali", "age": 20},        #ask yourself is this a lsit or a dictionary.
  #  {"name": "Hassan", "age": 18},              #it is a list. how to get the second item in a list        student [11]
 #   {"name": "Fatima", "age": 19}]

#print(students[1]["name"])                #don't forget how to get an item from a dic which is print(students ["name"]






#students = [{"name": "Ali", "age": 20},      
  #{"name": "Hassan", "age": 18},              
 # {"name": "Fatima", "age": 19}]

#for y in students:               #this one prints names of the students only. we can also get the ages by just changing the ["name"] to ["age"]
   # print(y["name"])


group = [{"name": "Cilmi", "job title": "employee"}, {"name":"Khadar", "job title": "manager"}]

for guys in group:
    print(guys["name"])   


#EXPLANATIIN

#Nested data structures means putting one data structure inside another. 
#For example, you can put a dictionary inside a list. 
#The list stores many dictionaries, and each dictionary stores information about one thing, such as a person. 
#First, you choose which dictionary you want by using the list index, like students[1]. 
#Then, because that item is a dictionary, you use its key to get the value, like students[1]["name"], which prints Hassan. 
#but
#If you use a for loop, Python goes through each dictionary one by one, so you use the loop variable (such as student) instead of writing an index. 
#Then you can get any value from the 
#current dictionary, for example student["name"] or student["age"].