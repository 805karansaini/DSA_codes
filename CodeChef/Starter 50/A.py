from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        x, y= [*map(int,input().split())]
        mid = (x+y)//2
        print( max( abs(mid-x), abs(mid-y)))
solve()# cook your dish here
