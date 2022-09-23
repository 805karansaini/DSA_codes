import bisect
from collections import defaultdict, deque
from functools import cache


def solve():
    N, K = [ *map(int,input().split()) ]
    nums = [ *map(int,input().split()) ]
    dic = defaultdict(int)
    if 2*K < len(nums):
        return "NO"
    
    for n in nums:
        dic[n] += 1
        if dic[n] == 3:
            return "NO"
    return "YES"


def solution():
    t = int(input())
    for i in range(t):
        temp = solve()
        print("Case #", end="")
        print(i+1,end="")
        if temp == "YES":
            print(": YES")
        else:
            print(": NO")

solution()