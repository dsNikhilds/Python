# Length of the input string

a = input("Enter your name ")
print("Length of " + a + " is ",len(a))


a= int(input("Enter a"))
b= int(input("Enter b"))

#Interchange a and b without using another variable

a = a + b
b = a - b
# a + b - b = a
a = a - b
# a + b -a = b

# print(a,b)

# Exercise

#1. Create a greeting for your program.

print("Welcome to the band name generator!")

#2. Ask the user for the city that they grew up in.

user_input1 = input("What's the name of the city you grew up in? \n")

#3. Ask the user for the name of a pet.

user_input2 = input ("What is the name of your pet? \n")

#4. Combine the name of their city and pet and show them their band name.

print("Your band name could be " + user_input1 + " " + user_input2)
