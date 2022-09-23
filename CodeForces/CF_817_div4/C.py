import bisect
from collections import defaultdict, deque, Counter
from functools import cache


def solve():
    N = int(input())
    s1 = input().split()
    s2 = input().split()
    s3 = input().split()
    ss1 = set(s1)
    ss2 = set(s2)
    ss3 = set(s3)
    ans = [0,0,0]
    for itm in ss1:
        if itm in ss2:
            if itm in s3:
                ss2.remove(itm)
                ss3.remove(itm)
            else:
                ss2.remove(itm)
                ans[0],ans[1] = ans[0]+1, ans[1] +1
        elif itm in ss3:
            ss3.remove(itm)
            ans[0],ans[2] = ans[0]+1, ans[2] +1
        else:
            ans[0] += 3
    
    for itm2 in ss2:
        if itm2 in ss3:
            ans[1], ans[2] = ans[1]+1,ans[2]+1
            ss3.remove(itm2)
        else:
            ans[1] = ans[1]+3
    ans[2] = ans[2] + (len(ss3) * 3)
    
    return ans
    


def solution():
    t = int(input())
    for i in range(t):
        temp = solve()
        print(" ".join(map(str,temp)))
        

solution()