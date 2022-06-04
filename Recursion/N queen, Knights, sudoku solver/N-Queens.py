def isSafe(board, r, c):
    # check in the column
    for i in range(r):
        if board[i][c] == True:
            return False
    # check diagonally left
    minLeft = min(r, c)
    for i in range(1,minLeft+1):
        if board[r - i][c - i] == True:
            return False

    # check diagonally left
    minRight = min(r, len(board) - c - 1)
    for i in range(1, minRight+1):
        if board[r - i][c + i] == True:
            return False

    return True


def displayboard(board):
    for i in board:
        for j in i:
            if j == False:
                print("X", end=" ")
            else:
                print("Q", end=" ")
        print()




def queen(board, r):
    if r == len(board):
        displayboard(board)
        print(" ")
        return 1

    count = 0
    for col in range(n):
        if isSafe(board,r,col):
            #place queen
            board[r][col] = True
            count += queen(board,r+1)
            #backtracking
            board[r][col] = False
    return count






n = 9
board = [ [False] * n for _ in range(n)]
print(queen(board, 0))