

def solve():
    t = int(input())
    while t:
        t-=1
        N, M= [*map(int,input().split())]
        nums= [*map(int,input().split())]
        nums.sort()
        flag = ["F"] * N
        total = [None] * (M*2)
        for n in nums():
            total[i] = n-1
            total[i+1] = n+1
        
        onlyright = set()
        onlyleft = set()
        infected = set(nums)
        for n in nums:
            if n+1 not in infected:
                flag[n+1] = "N"
                tempr = n
                break
            if n-1 not in infected:
                flag[n-1] = "N"
                templ = n
                break
        if tempr == -100:
            for n in nums:
                if n == templ:
                    onlyright.add(n)

                onlyright.add(n+1)
                onlyleft.add(n-1)
        else:


solve()
