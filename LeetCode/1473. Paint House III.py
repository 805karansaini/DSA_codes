# 1473. Paint House III
# https://leetcode.com/problems/paint-house-iii/
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
# Cost of paint the first and last house (10 + 1) = 11.

# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
# Output: -1
# Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], H: int, C: int, T: int) -> int:
        INF = 10 ** 20
        # H <= 100
        # C <= 20
        # target <= 100
        
        # index <= 100
        # last_color <= 20
        # neighborhoods <= 100
        
        has_cache = [[[False] * (T + 1) for _ in range(C + 1)] for _ in range(H + 1)]
        cache = [[[None] * (T + 1) for _ in range(C + 1)] for _ in range(H + 1)]
        
        # Total Time = Time per input * total inputs
        # Total inputs = ~ O(H * C * T) ~ 100 * 20 * 100 ~ 200,000
        # Each inputs = O(C)
        # Total time = O(H * C^2 * T) ~ 200,000 * 20 ~ 4,000,000
        def getMin(index, last_color, neighborhoods):
            if index == H:
                if neighborhoods == T:
                    return 0
                return INF
            if neighborhoods > T:
                return INF
            
            if has_cache[index][last_color][neighborhoods]:
                return cache[index][last_color][neighborhoods]
            
            has_cache[index][last_color][neighborhoods] = True
            
            if houses[index] == 0:
                ans = INF
                
                # some bruteforce things
                for current_color in range(1, C + 1):
                    if current_color == last_color:
                        ans = min(ans, getMin(index + 1, last_color, neighborhoods) + cost[index][current_color - 1])
                    else:
                        ans = min(ans, getMin(index + 1, current_color, neighborhoods + 1) + cost[index][current_color - 1])
                cache[index][last_color][neighborhoods] = ans
                return ans
            else:
                ans = None
                if houses[index] == last_color:
                    ans = getMin(index + 1, last_color, neighborhoods)
                else:
                    ans = getMin(index + 1, houses[index], neighborhoods + 1)
                cache[index][last_color][neighborhoods] = ans
                return ans
            
        ans = getMin(0, 0, 0)
        if ans >= INF:
            return -1
        return ans