# Connect 4 game
# 1 = first player ,  2 = second player , 0 = NO chip
num_row = 6
num_col = 7
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]
print("Lets play connect 4 -_-")
def Board():
    print("1 2 3 4 5 6 7")
    for row in range(0, num_row):
        for col in range(0, num_col):
            print(board[row][col], end=" ")
        print(" ")

def fillin(col, player):
    col = col - 1
    for rows in range(num_row-1, -1, -1):
        if board[rows][col] == 0:
            print("legal move")
            board[rows][col] = player
            break

def horizWin():
    # right to left
    for row in range(0, num_row):
        for col in range(0, 4):
            if board[row][col] > 0:
                if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                    quit(print("player", board[row][col], "win"))
    # left to right
    for row in range(0, num_row):
        for col in range(3, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row][col-1] == board[row][col-2] == board[row][col-3]:
                    quit(print("player", board[row][col], "win"))


def vertWin():
    # up to down
    for row in range(0, 3):
        for col in range(0, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                    quit(print("player", board[row][col], "win"))
    # down to up
    for row in range(3, num_row):
        for col in range(0, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row-1][col] == board[row-2][col] == board[row-3][col]:
                    quit(print("player", board[row][col], "win"))


def diagWin():
    # diag go up and to the right
    for row in range(3, num_row):
        for col in range(0, 4):
            if board[row][col] > 0:
                if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                    quit(print("player", board[row][col], "win"))
    # diag go down and to the right
    for row in range(0, 3):
        for col in range(0, 4):
            if board[row][col] > 0:
                if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                    quit(print("player", board[row][col], "win"))
    # diag go up and to the left
    for row in range(3, num_row):
        for col in range(3, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row-1][col-1] == board[row-2][col-2] == board[row-3][col-3]:
                    quit(print("player", board[row][col], "win"))
    # diag go down and to the left
    for row in range(0, 3):
        for col in range(3, num_col):
            if board[row][col] > 0:
                if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]:
                    quit(print("player", board[row][col], "win"))


def win():
    if horizWin() or vertWin() or diagWin():
        return True

player = 1
while not win():
    print("player", player, "turn", end=" ")
    col = int(input("Enter a column 1-7: "))
    if 0 < col < 8:
        fillin(col, player)
        Board()
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        continue