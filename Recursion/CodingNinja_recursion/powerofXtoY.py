import copy
import heapq
from re import I

def solve():
    t = int(input())
    while t:
        t-=1
        x , y = [*map(int,input().split())]
        def power(x,y):
            if y == 1:
                return x
            return x * power(x,y-1)
        print(power(x,y))
solve()
