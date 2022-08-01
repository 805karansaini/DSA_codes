from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        nums= [*map(int,input().split())]
        dic = {}

        for n in nums[::-1]:
            if n not in dic:
                dic[n] = 1
            elif n in dic:
                break

        print(len(nums)-len(dic))
solve()# cook your dish here
