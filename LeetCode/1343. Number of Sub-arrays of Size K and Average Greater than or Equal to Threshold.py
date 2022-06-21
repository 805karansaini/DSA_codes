# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        sm=0
        for i in range(k):
            sm+=nums[i]
        avg=sm//k
        count=0
        if avg>=threshold:
            count+=1
        for i in range(k,len(nums)):
            sm-=nums[i-k]
            sm+=nums[i]
            avg=sm//k
            if avg>=threshold:
                count+=1
        return count
    
    
#         N = len(nums)
#         low = high = res = sm = num = 0
#         while high < N:
            
#             while sm < k and high < N:
#                 num += nums[high]
#                 sm += 1
#                 if sm == k:
#                     #check for avg
#                     if num//k >= threshold:
#                         res += 1
#                 high += 1
            
#             num -= nums[low]
#             low += 1
#             sm -= 1
#         return res