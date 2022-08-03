from collections import Counter, defaultdict
import math
def solve():
    t = int(input())
    while t:
        t-=1
        x, y= [*map(int,input().split())]
        flag = True
        N = int(math.sqrt(y))
        for i in range(1, N):
            if y%i == 0:
                a = min(i,y//i)
                b = max(i,y//i)
                c = a-1
                d = x - c
                if d <= c:
                    if d < 0:
                        c,d = x, 0
                    print(a, b)
                    print(min(c,d), max(c,d))
                    flag = False
                    break
                
                c = b+1
                d = x-c
                if d>b:
                    print(a,b)
                    print(min(c,d), max(c,d))
                    flag = False
                    break

                if flag == False:
                    break
            if flag == False:
                break
        if flag:
            print(-1)
            

solve()# cook your dish here
