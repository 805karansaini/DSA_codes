def check(row, col, k):
    tempRow = row
    tempCol = col
    C_Count, R_Count = 0, 0

    # FOR COL
    if col == 0 or board[row][col-1] == 0:
        while tempCol < board_size and board[row][tempCol] == 1:
            C_Count += 1
            tempCol += 1

    # FOR ROW
    if row == 0 or board[row-1][col] == 0:
        while tempRow < board_size and board[tempRow][col] == 1:
            R_Count += 1
            tempRow += 1

    C_True, R_True = 0, 0
    if k == C_Count: C_True = 1
    if k == R_Count: R_True = 1 
    
    return R_True + C_True

def scrabbleWord(board_size, board, k):
    res = 0
    for R in range(board_size):
        for C in range(board_size):
            res += check(R, C, k)
            # print("Row : ", R, " ", "Col : ", C, " RES : ", res)
    return res

board_size = 5
board = [[0,0,1,0,0],[1,1,1,0,0],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,1]]
# board = [[1,1,1,0,0],[1,1,1,0,0],[1,1,1,1,1],[1,0,0,1,0],[1,1,1,1,1]]
# board = [[0,0,0,0,0],[1,1,0,0,0],[1,0,0,1,1],[1,0,0,1,0],[1,1,0,1,1]] 
k = 3
print("\n".join(map(str, board)))
print(scrabbleWord(board_size, board, k))