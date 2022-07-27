
def solve():
    t = int(input())
    while t:
        t-=1
        N =  int(input())
        
        if N == 1:
            print(1)
        elif N == 2:
            print(2,1)
        else:
            ans = [0]*N
            ans[0],ans[1] = 2,1
            i = 3
            j = 2
            for num in range(3,N+1):
                if num%2:
                    ans[i] = num
                    i+=2
                else:
                    ans[j] = num
                    j+=2
            print(" ".join(map(str,ans)))
solve()# cook your dish here
