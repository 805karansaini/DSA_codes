
def solve():
    t = int(input())
    while t:
        t-=1
        n =  int(input())
        nums = [*map(int,input().split())]
        
        if nums[0]==1:
            print("YES")
            continue
        else:
            flag = True
            for i in range(1,n):
                if nums[i] % nums[0] != 0:
                    print("NO")
                    flag = False
                    break

        if flag:
            print("YES")      
  
solve()