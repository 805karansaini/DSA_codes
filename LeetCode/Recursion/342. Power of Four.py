# 342. Power of Four
# https://leetcode.com/problems/power-of-four/
# Input: n = 16
# Output: true
# Input: n = 5
# Output: false

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = n

        def rec(n, base, power):
            num = pow(base, power)
            if n == num:
                return True
            if n < num:
                return False
            else:
                return rec(n, base, power + 1)

        return rec(num, 4, 0)