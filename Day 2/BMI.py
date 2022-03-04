# Body Mass Index

# Write a program which calculates a user's BMI using user's height and weight

# BMI = Weight/Height**2

weight = int(input("Enter your weight(kg) \n"))
height = float(input("Enter your height(m) \n"))
BMI = weight/(height**2)
print("Your BMI is {:.2f}".format(BMI))
#or
print(f"Your BMI is {BMI:.2f}") #This is a f-string