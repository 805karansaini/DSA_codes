def solve():
    t = int(input())
    while t:
        t-=1
        a, b = [*map(int,input().split())]
        c, d = [*map(int,input().split())]
        
        one = 0
        if a:
            one += 1
        if b:
            one += 1
        if c:
            one += 1
        if d:
            one += 1
        
        if one == 0:
            print("0")
        elif one == 4:
            print("2")
        else:
            print("1")

solve()