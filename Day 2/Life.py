# Write a program that tells us how many days, weeks, months we have left if we live until 75.

age = int(input("What is your current age\n"))
sub = 75-age # Remaining years
months = sub*12
weeks = sub*52
days = sub*365
print(f"Months left {months}\nWeeks left {weeks}\nDays left {days}")
