from collections import defaultdict
def solve():
    t = int(input())
 
    while t:
        t-=1
        n,m = [*map(int, input().split())]
        
        if (n+m) % 2:
            print("Burenka")
        else:
            print("Tonya")
       
solve()