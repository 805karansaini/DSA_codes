# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        n, m = [*map(int,input().split())]
        nums1 = input()
        nums2 = input()
        if m > n:
            print("NO")
            continue
        if m==n:
            if nums1 == nums2:
                print("YES")
            else:
                print("NO")
            continue

        back = 10**20
        for j in range(-1, -m-1, -1):
            if nums1[j] == nums2[j]:
                continue
            else:
                back = -j -1
                break
                
        if back == 10**20:
            print("YES")
            continue
        if len(nums2)-back > 1:
            print("NO")
            continue
        elif back == len(nums2):
            print("YES")
        else:
            temp = n-m
            makeset = set()
            for c in range(temp):
                makeset.add(nums1[c])
            
            if nums2[0] in makeset:
                print("YES")
            else:
                print("NO")

solve()# cook your dish here
