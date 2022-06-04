# 78. Subsets
# https://leetcode.com/problems/subsets/
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Input: nums = [0]
# Output: [[],[0]]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(p, up):
            liss = []
            if len(up) == 0:
                liss.append(p)
                return liss
            t = [up[0]]                 #imprt
            skip = sub(p, up[1:])
            comb = sub(p + t, up[1:])     #imprt
            skip.extend(comb)             #imprt

            return skip

        return sub([], nums)
