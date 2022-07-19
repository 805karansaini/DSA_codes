import sys
import heapq
# 1 1 2 3 5 8 17 
sys.setrecursionlimit(3000)
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        def fib(n):
            if n == 1:
                return 1
            if n == 2:
                return 1
            
            return fib(n-1) + fib(n-2)
        
        print(fib(n))

    # iterative
    ans = [1,1]
    for i in range(2,n):
        ans.append(ans[i-1]+ans[i-2])
    print(ans)
solve()
