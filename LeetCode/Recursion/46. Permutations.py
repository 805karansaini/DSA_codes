# 46. Permutations
# https://leetcode.com/problems/permutations/
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def per(p, up):
            liss = []
            if len(up) == 0:
                liss.append(p)
                return liss

            for i in range(len(up)):
                t = [up[i]]
                liss.extend(per(p + t, up[:i] + up[i + 1:]))  # first = pre() .... first.extend(first) wont work

            return liss

        return per([], nums)
