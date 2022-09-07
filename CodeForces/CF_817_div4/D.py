import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    N = int(input())
    s = input()
    maxsum = 0
    j = N
    k = N-1
    while j > 0:
        if j == 1:
            maxsum += (N//2)
            j -= 2
            continue
        maxsum += 2*(k)
        j-=2
        k -= 1

    ans, res = 0, []
    for i,c in enumerate(s):
        if c == "L":
            ans += i
            res.append((N-(i+1)) - i )
        else:
            ans += ((N-i)-1)
            res.append( i - (N-(i+1)))
        # print(res, i)
    res.sort(reverse=True)
    # print(ans, res)

    finalres = []
    for i in range(N):
        ans = max(ans, res[i]+ans)
        if ans < maxsum:
            finalres.append(ans)
        else:
            finalres.append(maxsum)
    return finalres


def solution():
    t = int(input())
    for i in range(t):
        temp = solve()
        print(" ".join(map(str,temp)))

solution()