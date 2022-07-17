import math

def solve():
    t = int(input())
    while t:
        t-=1
        want, have = [*map(int,input().split())]
        if want <= have:
            print("0")
            continue
        req = want - have
        packets = math.ceil(req/4)
        print(packets)
  
solve()