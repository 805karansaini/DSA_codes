from collections import defaultdict
def solve():
    def gcd(a,b):
        if (b == 0):
            return a
        return gcd(b, a%b)
    
    def celling(n, a):
        start = a
        last = 70000
    
        while start <= last:
            mid = (start + (last - start) // 2)
            val = gcd(a,mid)
            sq1 = a*a
            sq2 = mid*mid
            sqgdc = val*val
            lcm = ((a*mid)//val)
            sqlcm = lcm*lcm

            temp = sq1 + sq2 + sqgdc + sqlcm
            if n > temp:
                start = mid+1
            elif n < temp:
                last = mid-1
            if n == temp:
                ans.add((a,mid))
                ans.add((mid,a))
                start= mid +1
        return
    
 
    def floor(n, a):
        start = a
        last = 70000    
        while start <= last:
            mid = (start + (last - start) // 2)

            val = gcd(a,mid)
            sq1 = a*a
            sq2 = mid*mid
            sqgdc = val*val
            lcm = ((a*mid)//val)
            sqlcm = lcm*lcm

            temp = sq1 + sq2 + sqgdc + sqlcm
            if n > temp:
                start = mid+1
            elif n < temp:
                last = mid-1
            if n == temp:
                ans.add((a,mid))
                ans.add((mid,a))
                last = mid -1
        return

    t = int(input())
    while t:
        t-=1
        num = int(input())
        ans = set()
        for a in range(1,70000):
            floor(num,a)
            celling(num,a)
        print(len(ans), ans)
solve()