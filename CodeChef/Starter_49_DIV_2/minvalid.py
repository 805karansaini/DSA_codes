# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter


def solve():
    t = int(input())
    while t:
        t-=1
        
        nums=  [*map(int,input().split())]
        x,y,z = nums

        count = Counter(nums)
        mina = min(nums)
        maxb = max(nums)
        if count[x]==3:
            print("YES")
            continue
        if count[x] < 2 and count[y] < 2:
            print("NO")
            continue
        elif count[maxb] > count[mina]:
            print("NO")
        else:
            print("YES")

    
                

        
solve()# cook your dish here
