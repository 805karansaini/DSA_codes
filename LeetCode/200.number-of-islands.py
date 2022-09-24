#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [ (0,1),(1,0),(-1,0),(0,-1)  ]
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            for dx, dy in directions:
                dfs(dx+r, dy+c)
            return
        
        res = 0
        for r in range(R):
            for c in range(C):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        return res
# @lc code=end

