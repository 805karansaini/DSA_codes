import bisect
from collections import defaultdict, deque, Counter
def solve():
    N = int(input())
    nums = [ int(c) for c in input() ]
    count = Counter(nums)
    if count[1] == 0:
        print("0")
        return 

    res = nums[:]
    low = 0
    while low < N and res[low] == 1:
        low += 1

    if low < N:
        find_1 = 0
        while find_1 < N and nums[find_1] == 0:
            find_1 += 1

        
        for i,j in zip(nums, nums[find_1:]):
            if low >= N:
                break
            res[low] = (i | j)
            low += 1
    
    print("".join(map(str, res)))

    
    
            
            
solve()