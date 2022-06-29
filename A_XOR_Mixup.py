def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums = [*map(int,input().split())]
        nums.sort()
        
        for i in range(n):
            c = 0
            for j in range(n):
                if i==j:
                    continue
                c = c ^ nums[j]

            if c ==  nums[i]:
                print(nums[i])
                break
        
        
        

solve()