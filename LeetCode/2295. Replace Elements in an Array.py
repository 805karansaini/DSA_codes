# 2295. Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/

# Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
# Output: [3,2,7,1]
# Explanation: We perform the following operations on nums:
# - Replace the number 1 with 3. nums becomes [3,2,4,6].
# - Replace the number 4 with 7. nums becomes [3,2,7,6].
# - Replace the number 6 with 1. nums becomes [3,2,7,1].
# We return the final array [3,2,7,1].

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        lookup = defaultdict(int)
        for i, x in enumerate(nums):
            lookup[x] = i

        for i, j in operations:
            index = lookup[i]
            nums[index] = j
            del lookup[i]
            lookup[j] = index

        return nums