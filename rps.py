import random

def play_game(rounds):
    options = ('rock', 'paper', 'scissors')
    i = 0
    player_score = 0
    computer_score = 0

    while i < rounds:
        computer = random.choice(options)
        player = input("Enter your choice (rock, paper, scissors): ").lower()

        if player not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie.")
            i -= 1
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You won.")
            player_score += 1
        else:
            print("You lost.")
            computer_score += 1

        i += 1

    print("Final score:")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score > computer_score:
        print("Player wins the game! Congratulations.")
    else:
        print("Computer wins the game.")

# Main game logic
print("Welcome to Rock, Paper, Scissors Game.")
def main():
    print("Enter 1 for best of three.")
    print("Enter 2 for best of five.")
    play = int(input("Which one you wanna play? (1/2): "))

    if play == 1:
        print("You are playing best of 3.")
        play_game(3)
    elif play == 2:
        print("You are playing best of 5.")
        play_game(5)
    else:
        print("Invalid input.")
main()
