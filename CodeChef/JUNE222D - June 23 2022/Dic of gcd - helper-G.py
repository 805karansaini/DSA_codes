from collections import defaultdict
def solve():
    dic = defaultdict(int)
    def gcd(a,b):
        if (b == 0):
            return a
        return gcd(b, a%b)
    
    for i in range(100):
        for j in range(200):
            if (i,j) in dic:
                continue
            if (j,i) in dic:
                continue
            else:
                val = gcd(i,j)
                dic[(i,j)] = val
    print(dic)
solve()