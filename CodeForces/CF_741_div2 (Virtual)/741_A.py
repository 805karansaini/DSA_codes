def solve():
    t = int(input())
    while t:
        t-=1
        l, r = [*map(int,input().split())]
        ans1 = r//2 + 1
        if ans1 >= l:
            print(r-ans1)
        else:
            print(r%l)
        
    lis = seen.split()
solve()