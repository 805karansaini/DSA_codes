# 2294. Partition Array Such That Maximum Difference Is K
# https://leetcode.com/contest/weekly-contest-296/problems/partition-array-such-that-maximum-difference-is-k/
#
# Input: nums = [3,6,1,2,5], k = 2
# Output: 2
# Explanation:
# We can partition nums into the two subsequences [3,1,2] and [6,5].
# The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
# The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
# Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.
#
# Input: nums = [1,2,3], k = 1
# Output: 2
# Explanation:
# We can partition nums into the two subsequences [1,2] and [3].
# The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
# The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
# Since two subsequences were created, we return 2. Note that another optimal solution is to partition nums into the two subsequences [1] and [2,3].


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort(reverse=True)
        c = 0
        start = nums[0]
        for i in range(len(nums)):
            if start - nums[i] > k:
                c += 1
                start = nums[i]
        c += 1
        return c