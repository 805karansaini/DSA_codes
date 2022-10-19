import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    N = int(input())
    nums = [*map(int,input().split())]
    s = input()
    dic = {}

    for i,n in zip(s,nums):
        if n not in dic:
            dic[n] = i
        elif n in dic and dic[n] == i:
            pass
        else:
            return "NO"
    return "YES"




def solution():
    t = int(input())
    for i in range(t):
        temp = solve()
        if temp == "YES":
            print("YES")
        else:
            print("NO")

solution()