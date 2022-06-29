def solve():
    t = int(input())
    while t:
        t-=1
        n, k = [*map(int,input().split())]
        
        ans = max(n,k)
        print(ans)
solve()