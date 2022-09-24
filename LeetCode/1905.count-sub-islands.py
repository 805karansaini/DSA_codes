#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R, C = len(grid1), len(grid1[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c):
            if grid1[r][c] != grid2[r][c]:
                return 0
            grid2[r][c] = 0
            ans = 1
            for dx, dy in directions:
                nx, ny = dx+r, dy+c
                if 0 <= nx < R and 0 <= ny < C and grid2[nx][ny] == 1:
                    ans = dfs(nx,ny) and ans
            return ans
                
        res = 0
        for r in range(R):
            for c in range(C):
                if grid2[r][c]:
                    res += dfs(r,c)
        return res  
# @lc code=end

