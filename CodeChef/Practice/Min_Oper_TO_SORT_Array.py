# https://www.codechef.com/submit/PCJ18E
from collections import Counter, defaultdict
import math


def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        nums = [*map(int,input().split())]
        ans = sorted(nums[:])   
        
        i = 0 
        for num in nums:
            if num == ans[i]:
                i += 1
        print(N-i) 

        
solve()# cook your dish here
