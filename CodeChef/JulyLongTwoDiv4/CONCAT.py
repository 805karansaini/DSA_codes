# cook your dish here
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        nums =  [*map(int,input().split())]
        ans = sorted(nums)
        A = [ nums.index(ans[0]), 0]
        zero = [0]*n
        
        for i in range(2):
            A[0] = 0
            while A[0] < n:
                if nums[A[0]] == ans[A[1]] and not zero[A[0]] :
                    zero[A[0]] = 1
                    A[1] += 1
                    A[0] += 1
                else:
                    A[0] += 1
        if A[0] == A[1]:
            print("YES")
        else:
            print("NO")
           
solve()# cook your dish here
