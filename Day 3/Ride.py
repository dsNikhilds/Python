#Check if a person can ride the rollercoaster

height = input("Enter your height\n")

if int(height) > 120:
    print("You can ride it")
    age = int(input("What is your age?\n"))
    if age<12:
        bill = 5
        print("Your ticket fare is $5")
    elif age <=18:
        bill = 7
        print("Your ticket fare is $7")
    else:
        bill = 12
        print("Your ticket fare is $12")
    want_photo = input("Do you want photo? yes or no?\n")
    if want_photo.lower() == "yes":
        bill+=3
    print(f"Your total bill is ${bill}")
else:
    print("You can't ride it")