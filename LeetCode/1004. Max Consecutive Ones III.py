# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        if count[0] < k:
            return len(nums)
        if k == 0:
            best = 0
            res = 0
            for i in range(len(nums)):
                if nums[i]==1:
                    best += 1
                else:
                    res = max(res, best)
                    best = 0
            res = max(res, best)
            return res
        
        low = high = best = 0
        res = 0
        temp = k
        N = len(nums)
        while high < N:
            while temp > 0 and high < N:
                if nums[high] == 0:
                    temp -= 1
                best += 1
                high += 1
                
            while high < N and nums[high]==1 :
                best += 1
                high += 1
            # print(best, " : up")
            res = max(res, best)
            
            while temp  < 1 and low <= high:
                if nums[low] == 0:
                    temp += 1
                best -= 1
                low += 1
            # print(best, " after removing one 0")
        
        return res
# below solution is great i copied it from discussion
# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#       left = right = 0
      
#       for right in range(len(A)):
#         # if we encounter a 0 the we decrement K
#         if A[right] == 0:
#           K -= 1
#         # else no impact to K
        
#         # if K < 0 then we need to move the left part of the window forward
#         # to try and remove the extra 0's
#         if K < 0:
#           # if the left one was zero then we adjust K
#           if A[left] == 0:
#             K += 1
#           # regardless of whether we had a 1 or a 0 we can move left side by 1
#           # if we keep seeing 1's the window still keeps moving as-is
#           left += 1
      
#       return right - left + 1
                
                
                