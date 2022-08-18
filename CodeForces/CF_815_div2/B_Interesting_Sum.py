from collections import defaultdict

def solve():
    t = int(input())
 
    while t:
        t-=1
        n = int(input())
        nums = [*map(int, input().split())]
        nums.sort()
        print(nums[-1]+nums[-2]-nums[0]-nums[1])
        
solve()