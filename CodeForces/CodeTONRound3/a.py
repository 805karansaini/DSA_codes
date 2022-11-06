from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        nums = [*map(int,input().split())]

        if nums[0] == 1:
            print("Yes")
        else:
            print("No")
        
solve()