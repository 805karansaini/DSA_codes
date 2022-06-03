# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.dummy = matrix
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    self.dummy[i][j] = self.mat[i][j]
                    continue
                if i == 0:
                    self.dummy[i][j] = self.dummy[i][j - 1] + self.mat[i][j]
                    continue
                if j == 0:
                    self.dummy[i][j] = self.dummy[i - 1][j] + self.mat[i][j]
                    continue
                else:
                    self.dummy[i][j] = self.dummy[i][j - 1] + self.dummy[i - 1][j] + self.mat[i][j] - self.dummy[i - 1][
                        j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dummy[row2][col2]
        if row1 == 0:
            summ = self.dummy[row2][col2] - self.dummy[row2][col1 - 1]
            return summ
        if col1 == 0:
            summ = self.dummy[row2][col2] - self.dummy[row1 - 1][col2]
            return summ
        else:

            summ = self.dummy[row2][col2] - self.dummy[row1 - 1][col2] - self.dummy[row2][col1 - 1] + \
                   self.dummy[row1 - 1][col1 - 1]
            return summ

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)