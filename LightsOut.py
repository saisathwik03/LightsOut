import random

def initialize_grid():
    board = []
    for row in range(5):
        row = []
        for col in range(5):
            row.append(random.randint(0, 1))
        board.append(row)
    return board

def print_grid(board):
    for row in range(5):
        for col in range(5):
            print(board[row][col], end=" ")
        print()

def get_user_input():
    row = int(input("Enter the row to toggle the light: "))
    col = int(input("Enter the col to toggle the light: "))
    return row, col

def toggle_light(board, row, col):
    positions_to_toggle = [
        (row, col),     # The selected cell
        (row-1, col),   # The cell above
        (row+1, col),   # The cell below
        (row, col-1),   # The cell to the left
        (row, col+1),   # The cell to the right
    ]
    
    for i, j in positions_to_toggle:
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            board[i][j] = 1 if board[i][j] == 0 else 0
    return board

def check_win(board):
    for row in range(5):
        for col in range(5):
            if board[row][col] == 1:
                return False
    return True

def play_game():
    board = initialize_grid()
    while True:
        print_grid(board)
        row, col = get_user_input()
        toggle_light(board, row, col)
        if check_win(board):
            print("Congratulations! You've turned off all the lights.")
            print_grid(board)
            break

play_game()