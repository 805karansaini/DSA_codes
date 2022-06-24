# A is complementary to T.
# T is complementary to A.
# C is complementary to G.
# G is complementary to C.
def solve():
    t = int(input())
    while t:
        t-=1
        n = int(input())
        s = input()
        res = ""
        for chr in s:
            if chr == "A":
                res += "T"
            if chr == "T":
                res += "A"
            if chr == "C":
                res += "G"
            if chr == "G":
                res += "C"

        print(res)
solve()