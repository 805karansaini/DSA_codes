# 231. Power of Two
# https://leetcode.com/problems/power-of-two/
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Input: n = 16
# Output: true
# Explanation: 24 = 16

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = n

        def rec(n, base, power):
            num = pow(base, power)
            if num == n:
                return True
            if num > n:
                return False
            else:
                return rec(n, base, power + 1)

        return rec(num, 2, 0)

