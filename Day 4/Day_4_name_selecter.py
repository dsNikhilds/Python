# Write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill. 

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

import random
i = random.randint(0,len(names))
print("{} is going to pay the bill".format(names[i]))

#Write your code below this line 👇


