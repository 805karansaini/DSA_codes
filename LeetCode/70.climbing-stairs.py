#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [1,2]
        for _ in range(n-2):
            dp[0],dp[1] = dp[1], dp[0]+dp[1]
        return dp[1]        


# @lc code=end

