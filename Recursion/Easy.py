def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(6))


def bin(arr, s, l, t):
    m = s + (l-s)//2
    if arr[m] == t:
        return m
    if s > l:
        return -1
    elif arr[m] < t:
        return bin(arr, m+1, l, t)
    else:
        return bin(arr, s, m-1, t)


arr = [1,2,3,4,5,6,7,8,9]
t = 1
print(bin(arr, 0, len(arr)-1, t))

def sumOfDigits(n):
    if n == 0:
        return 0
    return (n % 10) + sumOfDigits(n // 10)

print(sumOfDigits(12034))

def prod(n):
    if n%10 == n:
        return n
    return (n%10) * prod(n//10)

print(prod(1234))
print(prod(12340))

global rev
def revNum(n):
    if n == 0:
        return
    rem = n%10
    rev = rev * 10 + rem
    revNum(n/10)
revNum(123405)
print(rev)
print(revNum(12345))