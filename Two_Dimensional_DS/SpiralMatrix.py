# https://leetcode.com/problems/spiral-matrix-ii/
# 59. Spiral Matrix II

def generateMatrix(n):
    matrix = [[i] * n for i in range(n)]

    count = 1
    rStart, cStart = 0, 0
    rEnd, cEnd = n - 1, n - 1

    while rStart <= rEnd and cStart <= cEnd:
        # fill the rows from left to right from cStart->cEnd
        for i in range(cStart, cEnd+1):
            matrix[rStart][i] = count
            count +=1
        rStart += 1

        # fill the col from top to bottom from rStart->rEnd
        for i in range(rStart, rEnd+1):
            matrix[i][cEnd] = count
            count += 1
        cEnd -= 1


        # fill all the row from right to left : cEnd->cStart
        if rStart < rEnd:
            for i in range(cEnd, cStart-1, -1): # take care of range (a,b,-1) a to b with -1 indexing
                matrix[rEnd][i] = count
                count += 1
            rEnd = rEnd - 1

        # fill all the col from down to up : rEnd -> rStart
        if cStart <= cEnd:
            for i in range(rEnd, rStart-1, -1): # take care of range (a,b,-1) a to b with -1 indexing
                matrix[i][cStart] = count
                count += 1
            cStart = cStart + 1

    return matrix


n = 5
print(generateMatrix(n))