# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

#     a  b
#     0, 1                n=0
#        1, 1             n=1
#           1, 2          n=2
#              2, 3       n=3
#                 3, 5    n=4


#         if n < 2:
#             return n
#         return self.fib(n-1) + self.fib(n-2)


