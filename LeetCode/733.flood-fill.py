#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        R = len(image)
        C = len(image[0])
        
        q = collections.deque()
        q.append((sr,sc))
        directions = [ (0,1),(1,0),(-1,0),(0,-1)  ]
        visited = set()
        while q:
            r, c = q.popleft()
            visited.add((r,c))
            image[r][c] = color

            for dx, dy in directions:
                if 0 <= r+dx < R and 0 <= c+dy < C and image[r+dx][c+dy] == target and (r+dx, c+dy) not in visited:
                    q.append((r+dx, c+dy))                 
        return image
# @lc code=end

