import copy
import heapq

#NOT SOLVED
def solve():
    def push(h, x):
        heapq.heappush(h, x)
    def pop(h):
        return heapq.heappop(h)

    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        
        h = [] 
        for num in nums:
            push(h, num)

        for _ in range(1,n):
            tq = []
            prev = pop(h)
            while h:
                curr = pop(h)
                var = curr - prev
                push(tq, var)
                prev = curr
            h = copy.deepcopy(tq) 
        
        print(h[0])
    

solve()