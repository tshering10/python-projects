import random
print("Welcome to the PIG Game.")
input("Are you ready? Press Enter to start the game.")

target = 10
player1_score = 0
player2_score = 0

def roll_dice():
    return random.randint(1,6)

while player1_score < target and player2_score < target:
    #player 1 turn
    print("Player 1's turn.")
    current_turn_score = 0
    while True:
        input("Press Enter to roll the dice: ")
        roll = roll_dice()
        print(f"Player 1 rolled {roll}.")
        
        if roll == 1:
            print("You rolled 1. Your turn is over and you lost your current turn score.")
            break
        
        current_turn_score += roll
        print(f"Current turn score: {current_turn_score}.")
        

        hold_score = input("Do you want to hold? (y/n): ").lower()
        if  hold_score == "y":
            player1_score += current_turn_score
            print(f"Player 1's total score: {player1_score}")
            break
        elif hold_score == "n":
            continue
        else:
            print("Invalid input.")
                   
    if player1_score >= target:
        print("Player 1 wins!!!")
        break
    
    #player 2
    print("Player 2 turn.")
    current_turn_score = 0
    while True:
        input("Press Enter to roll the dice: ")
        roll = roll_dice()
        print(f"Player 2 rolled {roll}.")
        
        if roll == 1:
            print("You rolled 1. Your turn is over and you lost your current turn score.")
            break
        
        current_turn_score += roll
        print(f"Current turn score: {current_turn_score}.")
        
        #   if roll != 1:
        #     p1_current_score += roll
        #     print(f"Your current score is {p1_current_score}")
        # else:
        #     print("You rolled 1. Your turn is over.")
        #     break
        
        hold_score = input("Do you want to hold? (y/n): ").lower()
        if  hold_score == "y":
            player2_score += current_turn_score
            print(f"Player 2's total score: {player2_score}")
            break
        elif hold_score == "n":
            continue
        else:
            print("Invalid input.")
                      
    if player2_score >= target:
        print("Player 2 wins!!!")
        break