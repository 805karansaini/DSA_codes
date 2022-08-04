from collections import Counter, defaultdict
import math
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        if n == 1:
            print(2)
            continue
        
        print(math.ceil(n/3))
    
solve()# cook your dish here
