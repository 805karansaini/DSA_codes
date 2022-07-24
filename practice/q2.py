def solve():
    t = int(input())
    while t:
        t-=1
        n,m =  [*map(int,input().split())]
        nums = [*map(int,input().split())]
        nums.sort()
        ans = []
        
        for i in range(m-n):
            temp = nums[-1]
            nums.append()
solve()