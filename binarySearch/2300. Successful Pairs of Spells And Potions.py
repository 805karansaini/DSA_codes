# 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]

import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0] * len(spells)
        potions.sort()
        print(potions)
        N = len(potions)

        for i, x in enumerate(spells):
            req = math.ceil(success / x)
            val = N
            start, end = 0, N - 1
            while start <= end:
                mid = start + (end - start) // 2
                if req <= potions[mid]:
                    val = mid
                    end = mid - 1
                else:
                    start = mid + 1
            res[i] = N - val
        return res

