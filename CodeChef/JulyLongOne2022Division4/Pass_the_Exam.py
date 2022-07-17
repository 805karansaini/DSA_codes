def solve():
    t = int(input())
    while t:
        t-=1
        A, B, C = [*map(int,input().split())]

        if (A+B+C)>= 100:
            if A >= 10 and B >= 10 and C >= 10:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("FAIL")
  
solve()