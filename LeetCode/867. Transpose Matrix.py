# 867. Transpose Matrix
# https://leetcode.com/problems/transpose-matrix/
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]


def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    R = len(matrix)
    C = len(matrix[0])
    mat = [[None] * R for _ in range(C)]
    for i in range(R):
        for j in range(C):
            mat[j][i] = matrix[i][j]
    return mat


arr = [[1,4],[2,5],[3,6]]
print(self.transpose(arr))
