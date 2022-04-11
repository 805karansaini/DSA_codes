# 1260. Shift 2D Grid
# https://leetcode.com/problems/shift-2d-grid/


class Solution(object):
    def shiftGrid(self, grid, k):

        m = len(grid)
        n = len(grid[0])

        if k % (m * n) == 0:
            return grid

        # make new grid using list comprehension
        grid2 = [[0] * n for _ in range(m)]

        for r in range(0, m):
            for c in range(0, n):
                oneDvalue = ((r * n + c) + k) % (m * n)
                # oneDvalue =  ((r*n+c)+k)
                # oneDshift = oneDvalue % (m*n)
                sRow = oneDvalue // n
                sCol = oneDvalue % n
                grid2[sRow][sCol] = grid[r][c]

        return grid2


