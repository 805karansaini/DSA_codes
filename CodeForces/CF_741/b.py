
from hashlib import new


def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        if N == 3:
            print(-1)
            continue
        nums = [0]*N
        mid = (N//2) +1
        new = 1
        for i in range(N):
            if mid <= N:
                nums[i] = mid
                mid += 1
            else:
                nums[i] = new
                new += 1
        
        print(" ".join(map(str,nums)))

solve()