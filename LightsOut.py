def Intialize_grid():
    board=[]
    for row in range(5):
        row=[]
        for col in range(5):
            row.append(0)
        board.append(row)
    return board

def print_grid(board):
    for row in range(5):
        for col in range(5):
            print(board[row][col],end=" ")
        print()

board=Intialize_grid()
print_grid(board)