import copy
import heapq
from re import I

#NOT SOLVED
def solve():
    def push(h, x):
        heapq.heappush(h, x)
    def pop(h):
        return heapq.heappop(h)

    t = int(input())
    while t:
        t-=1
        n, m  = [*map(int,input().split())]
        nums = [*map(int,input().split())]
        # first = i-1
        # last = m-i
        b = ["B"] * m 
        
        for i in nums:
            mini = min(i-1,m-i)
            if b[mini] == "B":
                b[mini] = "A"
            elif b[max(i-1,m-i)] == "B":
                b[max(i-1,m-i)] = "A"
            # elif b[min(i-1,m-i)] = "B":
            #     b[] = "A"
        
        print("".join(map(str,b)))

   

solve()