#tic-tac-toe game
def print_board(board):
    for i in range(0,3):
        print("  |  ".join(board[i]))
        if i < 2:
            print("-" * 15)
# board = [[" " for _ in range(3)] for _ in range(3)]
# print_board(board)

def check_win(board, player):
    #check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
            all([board[j][i] == player for j in range(3)]):
                return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to tic tac toe game.")
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn: ")
        try:
            row = int(input('Enter the row (0,1,2): '))
            row = int(input('Enter the row (0,1,2): '))