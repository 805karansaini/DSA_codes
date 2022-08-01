from collections import Counter, defaultdict

def solve():
    t = int(input())
    while t:
        t-=1
        s = input()
        n = int(input())
        str = []
        posi = {}
        for i in range(n):
            temp = input()
            str.append(temp)
            posi[temp] = i+1
        str = sorted(str, key=len, reverse=True)
        red = [False for i in range(len(s))]
        c = 0
        finalres = []
        breaked = False
        while c < len(s):
            localmax = []; localval = 0
            breaking = True
            tempmatch = False
            for st in str:
                for i in range(len(s)-len(st)+1):
                    if st == s[i:i+len(st)]:
                        breaking = False
                        count = Counter(red[i:i+len(st)])
                        temp = count[False]
                        if temp == len(st):
                            tempmatch = True
                            finalres.append([posi[st], i+1])
                            c += len(st)
                            for mark in range(i,i+len(st)):
                                red[mark] = True
                            break
                        if localval < temp:
                            change = True
                            localval = temp
                            localmax = [posi[st], i+1]
                if tempmatch:
                    break
            if tempmatch:
                continue
            if breaking:
                print(-1)
                breaked = True
            if localval > 0 and change:
                change = False
                finalres.append(localmax)
                c += localval
                for mark in range(localmax[1]-1,localmax[1]-1+len(st)):
                    red[mark] = True
            if breaked:
                break

        if not breaked:
            print(len(finalres))
            for i,j in finalres:
                print(i, j)
solve()# cook your dish here
