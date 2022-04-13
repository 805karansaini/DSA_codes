# https://leetcode.com/problems/pascals-triangle/submissions/
# 118. Pascal's Triangle
#
# Given an integer numRows, return the first numRows of Pascal's triangle.


def generate(numRows):
    n = numRows
    matrix = [[0] * i for i in range(1, n + 1)]

    for i in range(0, n):
        for j in range(0, i + 1):
            if j == 0 or j == i:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    return matrix


num = 5
print(generate(num))