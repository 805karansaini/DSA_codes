import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    N = int(input())
    s = input()
    word = "Timur"
    dic = Counter(s)
    dic2 = Counter(word)
    if len(s) != 5:
        return "NO"
    for i,j in dic2.items():
        if dic[i] >= j:
            continue
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