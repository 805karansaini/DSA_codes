# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums1 = input()
        nums2 = input()
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        
        for i in range(n):
            if nums1[i] == "0":
                count1["0"] += 1
            elif nums1[i]== "1":
                count1["1"] += 1
        for i in range(n):
            if nums2[i] == "0":
                count2["0"] += 1
            elif nums2[i]== "1":
                count2["1"] += 1
        diff1 = abs(count1["0"] - count2["0"])

        if (diff1)%2==1:
            print("0")
        else:
            print("1" )
solve()# cook your dish here
