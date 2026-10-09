#team = {"manager": "Axmed", "age": 40, "Won titles": "20"}
#print(type(team))
#print(team["age"])


#team = {"manager": "Axmed", "age": 40, "Won titles": "20"}
#for x in team:                                             This prints the door not the valuues inside it.
 #   print(x)                                 #But how can we tell python to give us the values nor the doors?

#here it is


#team = {"manager": "Axmed", "age": 40, "Won titles": 20}
#for key in team:
   # print(key)                     #here KEY isn't quoted becausue it is a variable not a string or something inside the dic
   # print(team["manager"])




#team = {"manager": "Axmed", "age": 40, "Won titles": 20}

#team ["lives"] = "Canada"
#team.clear ()
#for y in team.values():              #the different between for y in team:    and for y in team.value():
 # print(y)                           #Is that for y in team: will only print the keys. whle the other only prints the values




#team = {"manager": "Axmed", "age": 40, "Won titles": 20}

#team ["lives"] = "Canada"
#team.clear ()                         #now is used items and what has been changed. it prints each term to be a tuple and under each other.
#for y in team.items():                  #for exampleL  ("Age":  40)
 # print(y)







team = {"manager": "Axmed", "age": 40, "Won titles": 20}

for key, x in team.items():
  print(key)
  print(x)
