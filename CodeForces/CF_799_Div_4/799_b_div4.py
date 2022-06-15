from collections import defaultdict
def solve():
    t = int(input())
 
    while t:
        t-=1
        n = int(input())
        nums = [*map(int, input().split())]
        s = len(set(nums))
        if s%2 != n%2:
            s-=1
        print(s)
    return 
solve()