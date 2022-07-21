
def solve():
    t = int(input())
    while t:
        t-=1
        x =  int(input())
        nums = [*map(int,input().split())]
        
      
        ans = set()
        ans.add(x)
        
        for i in range(3):
            x = nums[x-1]
            ans.add(x)
            if x == 0:
                break
            
        
        if 1 in ans and 2 in ans and 3 in ans:
            print("YES")
        else:
            print("NO")
solve()