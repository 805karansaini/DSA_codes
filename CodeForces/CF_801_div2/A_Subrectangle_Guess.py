def solve():
    t = int(input())
    while t:
        t-=1
        n, m = [*map(int,input().split())]
        matrix = [ [] for i in range(n)]
        for i in range(n):
            temp = input().split()
            for j in temp:
                matrix[i].append(int(j))
        best = -10**20
        for i in range(n):
            for j in range(m):
                if matrix[i][j] > best:
                    x,y = [i+1,j+1]
                    best = matrix[i][j]
        # print((x*y),  ((n-x+1) * y ), ((m-y+1) * x ), ((m-y+1) * (n-x+1)))
        print(max( (x*y),  ((n-x+1) * y ), ((m-y+1) * x ), ((m-y+1) * (n-x+1))))
solve()