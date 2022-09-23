import bisect
from collections import defaultdict, deque, Counter


def solve():
    N = int(input())
    nums = [*map(int,input().split())]
    ans = nums[0]
    count = 0
    if ans == 0:
        count = 1
        ans = 639823
        
    for i in range(1,N):
        print(ans)
        if ans == nums[i] or nums[i] == 0:
            count += 1
            ans = 639823
        else:
            ans ^= nums[i]
    print(count)
    print()
    return
        


    



def solution():
    t = int(input())
    for i in range(t):
        solve()

solution()