from collections import Counter, defaultdict
import math
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [ i+1 for i in range(n)]
        print(n)
        print(" ". join(map(str,nums)))

        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
        for i in range(n-1):
            swap(i,i+1)
            print(" ". join(map(str,nums)))
solve()
