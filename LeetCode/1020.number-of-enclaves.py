#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        directions = [ (0,1),(1,0),(-1,0),(0,-1)  ]
        visited = set()

        def dfs(Rr,Cc):
            nonlocal tempres
            tempres += 1
            visited.add((Rr,Cc))
            ans = 1

            for dx,dy in directions:
                nx, ny = Rr+dx, Cc+dy
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    ans = 0
                    continue
                if grid[nx][ny] == 1 and (nx,ny) not in visited:
                    ans = dfs(nx,ny) and ans # i did it the wrong way as Ans = 0 it wont run DFS
            return ans
                
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    tempres = 0
                    flag = dfs(r,c)
                    if flag:
                        res += tempres
                    # print(r,c,res)
                    # print(flag, tempres, " flag tempres")
                    # print(visited)
        return res
# @lc code=end

