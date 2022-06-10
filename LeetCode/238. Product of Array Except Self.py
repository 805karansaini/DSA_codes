# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N

        prefix = 1
        for i in range(N - 1):
            prefix = prefix * nums[i]
            res[i + 1] = prefix
        postfix = 1
        for i in range(N - 1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]

        return res

        # suffix = 1
        # c = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         suffix *= nums[i]
        #     else:
        #         c += 1
        # if c > 1:
        #     return [0] * len(nums)
        # if c == 1:
        #     for i,j in enumerate(nums):
        #         if j==0:
        #             nums[i]=suffix
        #         else:
        #             nums[i]= 0
        # elif c<1:
        #     for i,j in enumerate(nums):
        #         nums[i]= suffix//j
        # return nums