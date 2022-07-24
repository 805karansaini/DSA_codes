# https://www.codechef.com/JULY222D/problems/SUMOFPROD1
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums =  [*map(int,input().split())]
        ans = []
        temp = 0
        for c in nums:
            if c == 1:
                temp +=1 
            else:
                ans.append(temp)
                temp = 0
        ans.append(temp)
        res = 0
        for c in ans:
            res += ((c * (c+1))//2)
        print(res)
solve()# cook your dish here
