from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        N,X= [*map(int,input().split())]
        
        if N > X:
            print(-1)
            continue
        ans = []
        ans.append(X-N+1)
        for i in range(1,N+1):
            if i != X-N+1:
                ans.append(i)
        print(" ". join(map(str,ans)))
solve()# cook your dish here
