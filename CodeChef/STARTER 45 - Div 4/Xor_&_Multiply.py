# answer copied
# https://www.codechef.com/viewsolution/67909764
tcs = int(input())
for tc in range(tcs):
    # nn = int(input())
    n, a, b = list(map(int, input().split()))
    x = 0
    pref = -1
    for i in range(n - 1, -1, -1):
        p = (1 << i) & a
        q = (1 << i) & b
        if p > 0 and q > 0:
            continue
        elif p == 0 and q == 0:
            x |= (1 << i)
        else:
            if pref == -1:
                if p == 0 and q > 0:
                    pref = 0
                else:
                    pref = 0
                    x |= (1 << i)
            else:
                if p == 0 and q > 0:
                    x |= (1 << i)
    print(x)