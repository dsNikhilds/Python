rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
hand = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user >= 3 or user < 0:
    print("Invalid choice!")
else:
    print(hand[user])
    computer_no = random.randint(0,2)
    computer = hand[computer_no]
    print("Computer chooses: \n",computer)
    
    if user == 0 and computer_no == 2:
        print("You won!")
    elif user== 0 and computer_no == 1:
        print("Computer won!")
    elif user== 1 and computer_no == 0:
        print("You won!")
    elif user== 1 and computer_no == 2:
        print("Computer won!")
    elif user== 2 and computer_no == 0:
        print("Computer won!")
    elif user== 2 and computer_no == 1:
        print("User won!")
    else:
        print("It is a tie!")