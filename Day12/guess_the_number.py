import random

def check(number,user, user2,life):
    
    if user2 > number:
        print("Too high")
        life -= 1
        if user =="easy":
            easy(number,user,life)
        else:
            difficult(number,user,life)
    if user2 < number:
        print("Too low")
        life -= 1
        if user =="easy":
            easy(number,user,life)
        else:
            difficult(number,user,life)
    else:
        print(f"You got it right, the answer was {number}")

def easy(number,user,life=10):
    print(f"You have {life} attempts left to guess the  number!")
    if life <= 0:
        return print("Game Over. You lost all lives!"   )

    user2 = int(input("Enter your guess \n"))
    check(number,user,user2,life)
    
def difficult(number,user,life=2):
    print(f"You have {life} attempts left to guess the  number!")
    if life <= 0:
        return print("Game Over. You lost all lives!")  
    user2 = int(input("Enter your guess \n"))
    check(number,user,user2,life)    
    
def difficulty():
    user = input("Choose a difficulty. Type 'Easy' or 'Hard'\n").lower()
    if user == "easy":
        easy(number,user)
    elif user == "hard":
        difficult(number,user)
    else:
        print("Input a valid option!")


print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100")
number = random.randint(1,100)
print("Secret number is ",number)
difficulty()
