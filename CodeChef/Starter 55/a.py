import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    X, Y = [*map(int,input().split())]
    Z = (3*X) - (X+Y)
    nums = [X,Y,Z]
    nums.sort()
    print(" ".join(map(str,nums)))


def solution():
    t = int(input())
    for i in range(t):
        solve()

solution()