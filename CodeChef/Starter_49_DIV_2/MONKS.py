# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter, defaultdict
import bisect
import math

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums=  [*map(int,input().split())]
        nums.sort(reverse=True)
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        if len(dic) == 1:
            print("0")
            continue
        summ = sum(nums) 
        mul = n
        for i in range(n):
            max = nums[i]
            if max*(mul-i) <= summ:
                ans = i
                break
        print(ans)
            


solve()# cook your dish here
