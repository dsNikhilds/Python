import random

def random_fn():
    return random.choice(cards)

def score_check(score,score_comp):
    print("Your cards: ",cards_user,"Total score: ",score)
    print("Computer cards: ",cards_comp,"Total score: ",score_comp)
    if score >21:
        print("You lose!")
        repeat = False
    elif score_comp >21:
        print("You win!")
        repeat = False
    elif score>score_comp:
        print("You win")
        repeat = False
    elif score == score_comp:
        print("Tie")
    else:
        print("You lose!")
        repeat = False
        


cards_user = []
cards_comp = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user1 = input("Do you want to play a game of blackjack? y or n? \n").lower()
repeat = True

if user1 =='y':
    a = random_fn()
    b = random_fn()
    cards_user.append(a)
    cards_user.append(b)
    score = sum(cards_user)
    print("Your cards: ",cards_user,"current score: ",score)
    comp1 = random_fn()
    comp2 = random_fn()        
    cards_comp.append(comp1)
    cards_comp.append(comp2)   
    score_comp = sum(cards_comp)             
    print(f"Computer's first card: {cards_comp}")
    while score_comp < 17:
        comp3 = random_fn()
        cards_comp.append(comp3)
    score_comp = sum(cards_comp)
    while repeat:        
        user2 = input("Type 'y' to get another card, type 'n' to pass.\n").lower()
        if user2=='n':
            score_check(score,score_comp)
            repeat = False
        elif user2 == 'y':
            c = random_fn()
            cards_user.append(c)
            score = sum(cards_user)
        #score_check(score,score_comp)

else:
        print("Have a nice day!")