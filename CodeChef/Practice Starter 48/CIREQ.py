# https://www.codechef.com/submit/CIREQ
from collections import Counter, defaultdict
from sortedcontainers import SortedList
import math

import sortedcontainers
# help(sortedcontainers)
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        nums.sort()
        sl = SortedList()
        sl.add(1)
        for n in nums:
            flag = True
            for i,index in enumerate(sl):
                if index <= n:
                    temp = sl.pop(i)
                    sl.add(temp+1)
                    flag = False
                    break
            if flag:
                sl.add(2)
        print(len(sl))
solve()