class Solution:
    def connectedComponents(n, connList):
        connList = [ *map(int, connList.split())]
        connections = []
        N = len(connList)
        for i in range(0,N,2):
            connections.append([ int(connList[i]), int(connList[i+1])])

        par = [ x for x in range(n)]
        rank = [ 1 for _ in range(n)]
        def find(n1):
            p = par[n1]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p1] += p2
            return 1

        res = 0
        for n1, n2 in connections:
            res += union(n1,n2)
        print(n-res)
    connectedComponents(int(input()), input())

            

