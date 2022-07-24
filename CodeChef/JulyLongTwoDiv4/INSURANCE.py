# https://www.codechef.com/JULY222D/problems/INSURANCE
def solve():
    t = int(input())
    while t:
        t-=1
        x,y =  [*map(int,input().split())]
        
        print(min(x,y))
solve()