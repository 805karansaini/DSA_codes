# 52. N-Queens II
# https://leetcode.com/problems/n-queens-ii/
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

class Solution:
    def totalNQueens(self, N: int) -> int:

        def tryrow(board, row, col_used, diag_1, diag_2):
            temp = 0
            if row == len(board):
                return 1

            for col in range(N):
                if col not in col_used and row - col not in diag_1 and row + col not in diag_2:
                    board[row][col] = "Q"
                    col_used.add(col)
                    diag_1.add(row - col)
                    diag_2.add(row + col)
                    temp += tryrow(board, row + 1, col_used, diag_1, diag_2)
                    diag_2.remove(row + col)
                    diag_1.remove(row - col)
                    col_used.remove(col)
                    board[row][col] = "."

            return temp

        board = [["."] * N for _ in range(N)]

        ans = tryrow(board, 0, set(), set(), set())

        return ans
