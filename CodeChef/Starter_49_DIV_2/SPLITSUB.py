# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter, defaultdict
import math


def solve():
    t = int(input())
    while t:
        t-=1
        N, k = [*map(int,input().split())]
        nums=  input()
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        if len(dic) == 1:
            print(math.ceil(N/k))
            continue
        if k == 1:
            print(abs(dic["0"] - dic["1"]))
            continue
        else:
            temp = abs(dic["0"] - dic["1"])
            print(math.ceil(temp/k))
    

        
solve()# cook your dish here
