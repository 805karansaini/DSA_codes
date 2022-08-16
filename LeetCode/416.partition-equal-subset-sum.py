#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:
            return False
        target //=2
        dp = set()
        dp.add(0)
        for n in nums:
            temp = set()
            for t in dp:
                if t+n == target:
                    return True
                temp.add(t)
                temp.add(t+n)
            dp = temp
        return False
# @lc code=end

