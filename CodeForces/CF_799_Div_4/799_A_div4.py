def solve():
    t = int(input())

    while t:
        t-=1
        c = 0
        nums = [*map(int,input().split())]
        for i in range(1,len(nums)):
            if int(nums[i])>int(nums[0]):
                c+=1
        print(c)
    return

solve()