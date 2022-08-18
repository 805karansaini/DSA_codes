from collections import defaultdict

def solve():
    t = int(input())
 
    while t:
        t-=1
        a,b,c,d = [*map(int, input().split())]

        if a*d == b*c:
            print("0")
            continue
        else:
            l,m = a*d, b*c

            if l!=0 and m%l== 0:
                print("1")
            elif m!=0 and l%m ==0:
                print("1")
            else:
                print("2")
        
solve()