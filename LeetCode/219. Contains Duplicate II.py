# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Input: nums = [1,0,1,1], k = 1
# Output: true


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)

        for i, c in enumerate(nums):
            if c in dic and i - dic[c] <= k:
                return True
            else:
                dic[c] = i
        return False
