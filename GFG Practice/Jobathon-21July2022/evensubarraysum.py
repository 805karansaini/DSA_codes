# https://practice.geeksforgeeks.org/contest/job-a-thon-11-hiring-challenge/problems/
class Solution:
    def solve(self,N,arr):
        for i in range(N-1):
            if (arr[i] + arr[i+1]) == 0:
                continue
            else:
                return "NO"
        return "YES"