
def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        nums = list(map(lambda x: [int(x)], input().split()))
        parts = N
        ans = 0
        while parts > 1:
            nexa = []
            for i in range(0,parts,2):
                l,r = nums[i],nums[i+1]
                if l[0] > r[0]:
                    l,r = r,l
                    ans += 1
                nexa.append(l+r)
            
            parts >>= 1
            nums = nexa
        print(ans if nums[0] == list(range(1,N+1)) else -1)

solve()