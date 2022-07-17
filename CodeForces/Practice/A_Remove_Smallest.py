def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        nums.sort()
        change = True
        while change:
            change = False
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] or abs(nums[i+1] - nums[i]) < 2:
                    nums[i] = -1000
                    change = True
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == -1000:
                    nums.pop(i)
        
        if len(nums) == 1:
            print("YES")
        else:
            print("NO")
        
        

solve()