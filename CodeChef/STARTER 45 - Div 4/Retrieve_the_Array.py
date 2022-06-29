from typing import Counter


def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        if n==1:
            temp = sum(nums)//2
            print(temp)
            continue
        diff = []
        for i in range(0,n-1):
            if i == 0:
                diff.append(nums[i+1] - nums[i])
            else:
                diff.append(diff[-1] + nums[i+1] - nums[i])
        
        var = nums[0] - sum(diff)
        var = var//(n+1)
        res = [0]*n
        for i in range(n):
            if i == 0:
                res[i] = var
            else:
                res[i] = var + diff[i-1]
        print(" ".join(map(str,res)))


solve()