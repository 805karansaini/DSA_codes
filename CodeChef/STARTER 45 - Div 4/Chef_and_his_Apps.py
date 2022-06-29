def solve():
    t = int(input())
    while t:
        t-=1
        S,X,Y,Z = [*map(int,input().split())]
        
        if X+Y+Z <= S:
            print("0")
            continue
        temp = min(X,Y)
        if temp+Z <= S:
            print("1")
        else:
            print("2")
solve()