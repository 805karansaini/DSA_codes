# 1984. Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        best = 10**20
        if N < 2:
            return 0
        low, high = 0, k-1
        print(nums)
        while high < N:
            # print(nums[high], nums[low])
            if (nums[high] - nums[low]) < best:
                best = nums[high] - nums[low]
                if best == 0:
                    break
            low += 1
            high += 1
        
        return best
        