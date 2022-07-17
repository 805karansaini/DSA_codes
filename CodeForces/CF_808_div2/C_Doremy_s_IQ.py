
def solve():
    t = int(input())
    while t:
        t-=1
        n, q = [*map(int,input().split())]
        v = [*map(int,input().split())]
        v1 = []
        
        ans = [0]* n
        hold = 0
        for i in range(n):
            if v[i] <=q and hold<q:
                ans[i] = 1
            else:
                hold+=1
                v1.append(i)
        
        while q and i<len(v1):
            ans[v1[i]] = 1
            i+=1
            q-=1

   
            

        print("".join(map(str,ans)))
        
  
solve()