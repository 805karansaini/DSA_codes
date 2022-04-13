# https://leetcode.com/problems/pascals-triangle-ii/
# 119. Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# return nth row.      i.e. 0th->1st->2nd->nth


def getRow(rowIndex):
    # return nth row.      i.e. 0th->1st->2nd->nth
    n = rowIndex + 1
    matrix = [[0] * i for i in range(1, n + 1)]

    for i in range(0, n):
        for j in range(0, i + 1):
            if j == 0 or j == i:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    return matrix[n - 1]

num = 2
print(getRow(num))
num = 5
print(getRow(num))