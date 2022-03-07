#  Write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
summ = 0
for item in student_heights:
    summ = summ + item
    average = summ/len(student_heights)
print(round(average))
