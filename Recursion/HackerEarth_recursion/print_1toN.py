import copy
import heapq
from re import I

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        def print1_n(n):
            if n == 0:
                return
            print1_n(n-1)
            print(n, end=" ")
        
        def printn_1(n):
            if n == 0:
                return    
            print(n, end=" ")
            printn_1(n-1)
            
        print1_n(n)
        print()
        printn_1(n)
solve()
