import bisect
from collections import defaultdict, deque, Counter


def solve():
    ball, boxes = [*map(int,input().split())]

    for i in range(1,boxes+1):
        if i > ball:
            print("NO")
            return
        else:
            ball -= i
    print("YES")
    return
        


def solution():
    t = int(input())
    for i in range(t):
        solve()

solution()