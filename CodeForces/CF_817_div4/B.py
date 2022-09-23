import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    N = int(input())
    s1 = input()
    s2 = input()
    for i,j in zip(s1,s2):
        # if i == j: continue
        # if i in "GB" and j in "GB":
        #     continue
        if i == "R" and j in "GB":
            return "NO"
        if j == "R" and i in "GB":
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