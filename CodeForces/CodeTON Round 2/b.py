from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        N, x= [*map(int,input().split())]
        nums= [*map(int,input().split())]
        u = -1; v = -1
        dp = [[u,v] for n in range(N+2)]
        v = 0
        ans = 0
        for i,n in enumerate(nums):
            if i == 0:
                dp[0][0] = n - x
                dp[0][1] = n + x
                continue
            low = n - x
            hi = n+x
            if low <= dp[i-1][0] <=  hi:
                dp[i][0] = max(dp[i-1][0],low)
                dp[i][1] = min(dp[i-1][1],hi)
                continue
            elif low  <= dp[i-1][1] <= hi:
                dp[i][0] = max(dp[i-1][0],low)
                dp[i][1] = min(dp[i-1][1],hi)
            else:
                ans += 1
                dp[i][0] = low
                dp[i][1] = hi

        print(ans)
solve()# cook your dish here
