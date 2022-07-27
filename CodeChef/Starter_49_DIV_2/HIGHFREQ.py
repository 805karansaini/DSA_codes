# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter, defaultdict
import math


def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums=  [*map(int,input().split())]
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        if len(dic)==1:
            for key, val in dic.items():
                print(math.ceil(val/2))
                continue
        else:
            c = 0
            for key, val in dic.items():
                if c == 0:
                    key1 = key
                    val1 = val
                if c == 1:
                    key2 = key
                    val2 = val
                c += 1
                if c == 2:
                    break
            ans = max(math.ceil(val1/2),val2)
            print(ans)
        

    
                

        
solve()# cook your dish here
