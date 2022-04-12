# https://leetcode.com/problems/set-matrix-zeroes/submissions/
# 73. Set Matrix Zeroes
# optimized in place




def setZeroes(matrix):
    RowZero = False # make a temp variable to flag if matrix[0][0] is zereo or not its for making row[0][] = 0
    for i in range(len(matrix)): # set 1st row and 1st column to zero if want to change those row and col to zero
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    RowZero = True

# for col (1-last) change all {col = 0} (not the 0th col) // because they store the value for row change
    for j in range(1,len(matrix[0])):
        if matrix[0][j] == 0:  # change all the col to value 0 for having value = 0
            for k in range(len(matrix)):
                matrix[k][j] = 0


    #change all rows (1,last) = 0.  if 0th column tells to do
    for j in range(1,len(matrix)):
        if matrix[j][0] == 0:  # change all the row to value 0 for having value = 0
            for k in range(len(matrix[0])):
                matrix[j][k] = 0

    #change the 0th columns value = 0 if matrix[0][0] = 0  //was skipped earlier
    if matrix[0][0] == 0:
        for j in range(len(matrix)):
            matrix[j][0] = 0

    # change 0th Row = 0.  if RowZero = True
    if RowZero == True:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)


