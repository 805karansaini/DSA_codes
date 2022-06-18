def solve():
    INF = 10**20
    t = int(input())
    while t:
        t-=1
        n = int(input())
        piles = [*map(int,input().split())]
        
        if n%2==1:
            print("Mike")
            continue
        mike1, indx1 = INF, 0
        joe1, indx2 = INF, 1
        for i in range(n):
            if i%2==0:
                if mike1 < piles[i]:
                    mike1 =piles[i]
                    indx1 = i
            else:
                if joe1 < piles[i]:
                    joe1 =  piles[i]
                    indx2 = i
       
        if mike1 > joe1:
            print("Mike")
        elif mike1 < joe1:
            print("Joe")
        else:
            if indx1 > indx2:
                print("Mike")
            else:
                print("Joe")
solve()