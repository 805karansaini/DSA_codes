from collections import defaultdict
import copy
import heapq
from re import I

#NOT SOLVED
def solve():
   
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        ans = [0]*n
        dic = defaultdict(list)
        for i,x in enumerate(nums):
            dic[x].append(i) 
        # print(dic)
        for i, j in dic.items():
            maxi = 0
            prev = j[0]
            curr = 1
            for idx in j:
                if (prev-idx)%2 == 1 or (prev-idx) == 1:
                    curr += 1
                else:
                    pass
                if curr > maxi:
                    maxi = curr
                prev = idx
            ans[i-1] = maxi
        # printt = 
        print(" ".join(map(str,ans)))
                    

solve()