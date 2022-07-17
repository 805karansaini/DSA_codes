import math

def solve():
    t = int(input())
    while t:
        t-=1
        test, n, nsum = [*map(int,input().split())]
        ans = 0
        while test:
            test -= 1
            temp = min(n,nsum)
            nsum -= temp
            ans += (temp*temp)
            if nsum == 0:
                break
        print(ans)
  
solve()