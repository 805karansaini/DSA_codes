# 2293. Min Max Game
# https://leetcode.com/contest/weekly-contest-296/problems/min-max-game/
# Input: nums = [1,3,5,2,4,8,2,2]
# Output: 1
# Explanation: The following arrays are the results of applying the algorithm repeatedly.
# First: nums = [1,5,4,2]
# Second: nums = [1,4]
# Third: nums = [1]
# 1 is the last remaining number, so we return 1.

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        flag = 1
        temp = nums[:]
        while len(nums) > 1:
            j = 0
            temp = []
            for i in range(0, len(nums) - 1, 2):
                if flag == 1:
                    temp.append(min(nums[i], nums[i + 1]))
                    j += 1
                    flag = 0
                elif flag == 0:
                    temp.append(max(nums[i], nums[i + 1]))
                    j += 1
                    flag = 1
            nums = temp[:]
        return nums[0]