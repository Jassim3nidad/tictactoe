import random

def display_board(board):
    """Displays the tic-tac-toe board."""
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def check_victory(board, sign):
    """Checks if a player (or the computer) has won."""
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(row[col] == sign for row in board):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def is_full(board):
    """Checks if the board is full."""
    return all(all(cell in ['X', 'O'] for cell in row) for row in board)

def computer_move(board):
    """Determines the computer's move and updates the board."""
    empty_squares = [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['X', 'O']]
    move = random.choice(empty_squares)
    board[move[0]][move[1]] = 'X'

def user_move(board):
    """Prompts the user for their move and updates the board."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError("Move must be between 1 and 9.")
            row, col = divmod(move, 3)
            if board[row][col] in ['X', 'O']:
                raise ValueError("Square already occupied. Choose another.")
            board[row][col] = 'O'
            break
        except ValueError as e:
            print(e)

# Initialize the game board
board = [[str(3 * row + col + 1) for col in range(3)] for row in range(3)]
board[1][1] = 'X'  # Computer starts in the middle

# Main game loop
print("Welcome to Tic-Tac-Toe!")
display_board(board)
while True:
    user_move(board)
    display_board(board)
    if check_victory(board, 'O'):
        print("Congratulations, you win!")
        break
    if is_full(board):
        print("It's a tie!")
        break
    computer_move(board)
    display_board(board)
    if check_victory(board, 'X'):
        print("Sorry, the computer wins!")
        break
    if is_full(board):
        print("It's a tie!")
        break
