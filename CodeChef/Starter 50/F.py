from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        N,X,Y= [*map(int,input().split())]
        nums = [*map(int,input().split())]
        
        if Y >= X:
            print( ( max(nums)+Y-1 )//Y )
            continue
        temp = [0]*N
        temp[0] = nums[0]

        for i in range(1,N):
            temp[i] = max(temp[i-1],nums[i])
        
        ans = 0
        for i in range(N-1, -1, -1):
            operY = (nums[i] + Y-1) // Y
            if ans >= operY:
                continue
            else:
                operPer = operY - ans
                var = nums[i] - Y * ans
                xanseq = (var + X - 1) // X
                xoperation = min(xanseq,operPer)
                yoperation = max( (nums[i] - X * xoperation+Y-1 )//Y, ans)
                ans = max( ans, xoperation + yoperation)
        print(ans)

solve()# cook your dish here
