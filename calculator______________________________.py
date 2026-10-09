print ("Hello")


numb = int(input("First number"))
numb1= int(input("Second number"))

operation = input("Choose operation: +, -, *, /")


if operation == "+":
    print (numb + numb1)
elif operation == "-":
    print (numb - numb1)
elif operation == "*":
    print (numb * numb1)
elif operation == "/":
    print (numb / numb1)

else:
    print ("Invalid operation")