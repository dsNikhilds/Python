#


print("Welcome to the calculator")
bill = float(input("What was your total bill?\n"))
tip = int(input("What % of tip would you like to give? 10, 12, or 15?\n"))
calc_tip = bill*(tip/100)
people = int(input("How many people to split the bill?"))
total_bill = bill + calc_tip

if people>1:
    print(f"Each person needs to pay {round(total_bill/people,2)}$")
else:
    print(f"Your bill is {round(total_bill,2)}$")