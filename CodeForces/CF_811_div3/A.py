from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        N,H,M= [*map(int,input().split())]
        nums = []
        for i in range(N):
            h, m = [*map(int,input().split())]
            nums.append((h*60) + m)
        
        nums.sort()
        time = (H*60) + M
        flag = True
        for i in nums:
            if i < time:
                continue
            else:
                ttime = i - time
                th = ttime//60
                tm = ttime%60
                print(th, tm)
                flag = False
                break
        if flag:
            i = nums[0]
            ttime = ( 24*60) + ( i) - time 
            th = ttime//60
            tm = ttime%60
            print(th, tm)
solve()# cook your dish here
