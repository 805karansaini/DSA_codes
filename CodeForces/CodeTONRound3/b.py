# from collections import Counter, defaultdict
# from itertools import groupby

def solve():
    t = int(input())
    while t:
        t-=1
        N = int(input())
        s = input()
        zero = 0
        one = 0

        prev = s[0]
        count = 0
        zeros, ones = 0,0
        for c in s:
            if c == "0":
                zeros+=1
            else:
                ones += 1
            if prev == c:
                count += 1
            else:
                if prev == "0":
                    if zero <= count:
                        zero = count
                if prev == "1":
                    if one <= count:
                        one = count
                count = 1
                prev = c
        if prev == "0":
            if zero <= count:
                zero = count
        if prev == "1":
            if one <= count:
                one = count
        res = max( zero*zero, zeros*ones, one*one)
        print(res)
solve()