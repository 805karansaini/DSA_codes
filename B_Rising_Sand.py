def solve():
    t = int(input())
    while t:
        t-=1
        n, k = [*map(int,input().split())]
        nums = [*map(int,input().split())]
        
        if k == 1:
            ans = n-2
            ans = (ans+1)//2
            print(ans)
            continue
        else:
            res = 0
            for i in range(1,n-1):
                # print(nums[i-1], nums[i], nums[i+1])
                if nums[i] > nums[i-1] + nums[i+1]:
                    res += 1
            print(res)

solve()