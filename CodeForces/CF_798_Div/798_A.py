def solve():
    t = int(input())

    while t:
        t-=1
        temp = input().split()
        m = int(temp[0])
        n = int(temp[1])
        k = int(temp[2])
        str1 = input()
        str2 = input()
        res = ""
        str1 = ''.join(sorted(str1, reverse=True))
        str2 = ''.join(sorted(str2, reverse=True))
        # print(str1)
        # print(str2)
        k1 = 0
        k2 = 0
        while m and n:
            if (k2==k) or ( str1[m-1] <= str2[n-1] and k1 < k ):
                res += str1[m-1]
                m-=1
                k1+=1
                k2 = 0
            elif (k1==k) or ( str1[m-1] >= str2[n-1] and k2 < k ):
                res += str2[n-1]
                n -= 1
                k2 += 1
                k1 = 0
            # print(m,n, " : ", res)
        print(res)

solve()