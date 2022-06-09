# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


class Solution(object):
    def twoSum(self, nums, target):
        low, high = 0, len(nums) - 1

        while low < high:
            if (nums[low] + nums[high]) < target:
                low += 1
            elif (nums[low] + nums[high]) > target:
                high -= 1
            elif (nums[low] + nums[high]) == target:
                return [low + 1, high + 1]

        return [-1, -1]

