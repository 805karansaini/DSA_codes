import bisect
from collections import defaultdict, deque, Counter


def solve():
    nums = [*map(int,input().split())]
    nums.sort()
    res = [1,0,1,4]
    ans = 1
    for i in range(30):
        x = ((nums[0]>>i)&1)
        y = ((nums[1]>>i)&1)
        z = ((nums[2]>>i)&1)
        ans = (ans*res[x+y+z])
    print(ans)



def solution():
    t = int(input())
    for i in range(t):
        solve()

solution()