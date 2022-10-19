import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    N, Q = [*map(int,input().split())]
    nums = [*map(int,input().split())]
    queries = []
    for i in range(Q):
        queries.append( [*map(int,input().split())])
    
    odd = 0 
    even = 0
    cE, cO = 0, 0
    for n in nums:
        if n%2==1:
            odd += n
            cO += 1 
        else:
            even += n 
            cE += 1 
    res = []
    for x,v in queries:
        if x == 0:
            temp = cE * v
            if v % 2 == 0:
                even += temp
            else:
                cO += cE
                odd += (even + temp)
                even = 0
                cE = 0
        else:
            temp = cO * v
            if v % 2 == 0:
                odd += temp
            else:
                cE += cO
                even += (odd + temp)
                odd = 0
                cO = 0
        # print(cE, even, "", cO, odd)
        print(even + odd)

                
    return 0






def solution():
    t = int(input())
    for i in range(t):
        # print("TC : ", i+1)
        temp = solve()
    

solution()