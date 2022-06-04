# 51. N-Queens
# https://leetcode.com/problems/n-queens/
# Input: n = 4
# Output: [[".Q..","...Q",
#           "Q...","..Q."],
#          ["..Q.","Q...",
#           "...Q",".Q.."]]


#very optimized
class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        ans = []

        def tryrow(board, row, col_used, diag_1, diag_2):
            if row == len(board):
                lis = []
                for r in board:
                    lis.append("".join(r))
                ans.append(lis)
                return

            for col in range(N):
                if col not in col_used and row - col not in diag_1 and row + col not in diag_2:
                    board[row][col] = "Q"
                    col_used.add(col)
                    diag_1.add(row - col)
                    diag_2.add(row + col)
                    tryrow(board, row + 1, col_used, diag_1, diag_2)
                    diag_2.remove(row + col)
                    diag_1.remove(row - col)
                    col_used.remove(col)
                    board[row][col] = "."

        board = [["."] * N for _ in range(N)]

        tryrow(board, 0, set(), set(), set())

        return ans

