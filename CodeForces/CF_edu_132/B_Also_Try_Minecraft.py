def solve():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    
    pref_f = [0]*n
    pref_b = [0]*n
    
    for i in range(n-1):
        d = h[i]-h[i+1]
    
        if d > 0:
            pref_f[i+1] = d
        else:
            pref_b[i+1] = -d
    
        pref_f[i+1] += pref_f[i]
        pref_b[i+1] += pref_b[i]
    
    for _ in range(m):
        s, t = map(int, input().split())
    
        if s < t:
            print(pref_f[t-1] - pref_f[s-1])
        else:
            print(pref_b[s-1] - pref_b[t-1])
solve()