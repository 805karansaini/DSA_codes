# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = collections.defaultdict(set)  # key r//3,j//3
        for r in range(9):
            row = set()
            col = set()
            for c in range(9):
                # check for rows and square
                if board[r][c] == ".":
                    pass
                elif (board[r][c] in row or
                      board[r][c] in square[(r // 3), (c // 3)]):
                    return False
                square[(r // 3, c // 3)].add(board[r][c])
                row.add(board[r][c])

                # check for col
                if board[c][r] == ".":
                    continue
                elif board[c][r] in col:
                    return False
                col.add(board[c][r])

        return True