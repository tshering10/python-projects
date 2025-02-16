def print_board(board):
    """Print the current state of the game board."""
    for i in range(0, 3):
        print("  |  ".join(board[i]))
        if i < 2:
            print("-" * 15)

def check_win(board, player):
    """Check if the current player has won."""
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """Check if the game board is full."""
    return all([cell != " " for row in board for cell in row])

def play_game():
    """Run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to the Tic-Tac-Toe game.")
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn: ")
        
        # Input validation for row and column
        valid_move = False
        while not valid_move:
            try:
                row = int(input('Enter the row (0, 1, 2): '))
                col = int(input('Enter the column (0, 1, 2): '))
                
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    board[row][col] = current_player
                    valid_move = True
                else:
                    print("Invalid move! The cell is either occupied or out of bounds. Try again.")
            except ValueError:
                print("Invalid input! Please enter integers for row and column between 0 and 2.")

        # Print the updated board
        print_board(board)

        # Check for win or draw
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Uncomment to run the game
# play_game()
