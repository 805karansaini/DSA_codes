
from functools import cache


D = int(input())
k = int(input())
def minDays(D,k):
    def prime(i, primes):
        for prime in primes:
            if not (i == prime or i % prime):
                return False
        primes.add(i)
        return i

    def N_prime(n):
        primes = set([2])
        i, p = 2, 0
        while True:
            if prime(i, primes):
                p += 1
                if p == n:
                    return primes
            i += 1

    nums = list(N_prime(k))
    nums.reverse()
    print(nums)
    res = -1

    @cache
    def recur(total,i,j):
        if total == D:
            print("true")
            nonlocal res
            res = j
            return True
        if D < total or i >= len(nums):
            return False

        return recur(total+nums[i],i,j+1) or recur(D,i+1,j)

    recur(0,0,1)
    return res
print(minDays(D,k))


