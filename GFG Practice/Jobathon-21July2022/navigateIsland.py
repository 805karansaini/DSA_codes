# https://practice.geeksforgeeks.org/contest/job-a-thon-11-hiring-challenge/problems/
from collections import defaultdict
import heapq
from typing import List
class Solution:
    def minimumCost(self, N, M, X , A, B) -> int:
        INF = 10**20
        dic = defaultdict(list)
        for i,j in B:
            dic[i].append(j)
            dic[j].append(i)
        
        var = [INF]*N
        pq = [(0,1)]
        heapq.heappush(pq, (A[0] + A[N-1] + X, N))
        
        while pq:
            cost, un = heapq.heappop(pq)
            
            if un == N:
                return cost
            if var[un] <= cost:
                continue
            var[un] = cost
            
            for v in dic[un]:
                ans = cost + A[un-1] + A[v-1]
                heapq.heappush(pq,(ans,v))
        
        return -1

