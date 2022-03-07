# Write a program that calculates the highest score from a List of scores. 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

#print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
a = 0
for item in student_scores:
    if a > item:
        pass
    else:
        a = item
print("Highest score in the class is: ",a)