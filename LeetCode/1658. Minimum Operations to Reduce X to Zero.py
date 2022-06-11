# 1658. Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1

        suffix_seen = {}
        suffix_seen[0] = 0

        current = 0
        for i, x in enumerate(reversed(nums), 1):
            current += x
            suffix_seen[current] = i

        INF = 10 ** 20
        best = INF
        if target in suffix_seen:
            best = min(best, suffix_seen[target])

        current = 0
        for i, x in enumerate(nums, 1):
            current += x
            # target = current + some suffix
            # target - current = some suffix
            if target - current in suffix_seen:
                best = min(best, suffix_seen[target - current] + i)
        if best == INF:
            return -1
        return best