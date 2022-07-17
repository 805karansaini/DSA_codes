
def solve():
    t = int(input())
    while t:
        t-=1
        n, l, r = [*map(int,input().split())]
        f = 0
        nums = []

        for i in range(1,n+1):
            low = l//i
            high = r//i

            low*=i
            high *=i
            if high < l or low > r:
                f = 1
                break
            else:
                nums.append(high)
           
        if f == 0:
            print("YES")
            print(" ".join(map(str,nums)))
        else:
            print("NO")
  
solve()