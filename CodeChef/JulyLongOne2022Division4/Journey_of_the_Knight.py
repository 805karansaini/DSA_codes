import math

def solve():
    t = int(input())
    while t:
        t-=1
        x1, y1, x2, y2 = [*map(int,input().split())]
        c1 = abs(x1-x2)
        c2 = abs(y1-y2)

        if(c1%2==c2%2):
            print("YES")
        else:
            print("NO")
solve()
