# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Input: nums = [1,0,1,1,0,1]
# Output: 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                best += 1
                if best > res:
                    res = best
            else:
                best = 0          
        return res
                
        