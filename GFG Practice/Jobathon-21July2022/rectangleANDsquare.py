# https://practice.geeksforgeeks.org/contest/job-a-thon-11-hiring-challenge/problems/
class Solution:
    def minimumMoves(self, A : int, B : int) -> int:
        total = A*B
        c = 0
        
        while total != 0:
            C = min(A,B)
            D = max(A,B)
            c +=1
            total = total - (C*C)
            A = C
            B = D - C
        return c
            