# https://www.codechef.com/JULY222D/problems/OFFICE
def solve():
    t = int(input())
    while t:
        t-=1
        x,y =  [*map(int,input().split())]
        print((4*x) + y)
solve()